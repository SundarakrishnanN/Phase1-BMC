import pandas as pd
from ultralytics import YOLO
import customCounter2 as solutions
import cv2
import time
import numpy as np

# Initialize YOLO model
model = YOLO(r"v3_results\kaggle\working\runs\detect\train\weights\best.pt")

# Video file path
video_file = r'data\Stn_HD_1_time_2024-05-20T07_30_02_002.mp4'

# Desired output resolution
new_width = 1000  # New width
new_height = 1000  # New height

# Open video capture
cap = cv2.VideoCapture(video_file)

# Check if video capture is open
assert cap.isOpened(), "Error reading video file"

# Get actual video resolution
video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Get video frame rate (FPS)
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Video frame rate (FPS): {fps}")

# Define region points for object counting
regions = {

    'J1':[(0, 0), (new_width//8, 0), (new_width//8, new_height), (0, new_height)],

    'J2':[(new_width//8, 0), (7*new_width//8, 0), (7*new_width//8, new_height//5), (new_width//8, new_height//5)],
    
    'J3':[(7*new_width//8, 0), (new_width, 0), (new_width, new_height), (7*new_width//8, new_height)]

}

# Define vehicle classes
vehicle_classes = ['car', 'bus', 'truck', 'three-wheeler', 'two-wheeler', 'lcv', 'bicycle']

# Initialize counters for each region
counterJ1 = solutions.ObjectCounter(
    view_img=False,
    reg_pts=regions['J1'],
    names=model.names,
    draw_tracks=True,
    line_thickness=2
)
counterJ2 = solutions.ObjectCounter(
    view_img=False,
    reg_pts=regions['J2'],
    names=model.names,
    draw_tracks=True,
    line_thickness=2
)
counterJ3 = solutions.ObjectCounter(
    view_img=False,
    reg_pts=regions['J3'],
    names=model.names,
    draw_tracks=True,
    line_thickness=2
)

# Helper function to draw regions on the image for visualization
def draw_regions(image, regions):
    for region, points in regions.items():
        points = [(int(x), int(y)) for x, y in points]
        cv2.polylines(image, [np.array(points)], isClosed=True, color=(0, 255, 0), thickness=2)
        center_x = int((points[0][0] + points[2][0]) / 2)
        center_y = int((points[0][1] + points[2][1]) / 2)
        cv2.putText(image, region, (center_x, center_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return image

# Create resizable window
cv2.namedWindow('Object Detection', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Object Detection', video_width, video_height)

# Time tracking for processing
last_processed_time = time.time()

# Main video processing loop
while cap.isOpened():
    # Read a frame
    success, im0 = cap.read()
    
    # If no frame read, break the loop
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    # Get current time
    
    
    # Check if it's time to process a new frame
    # Process once per second
        # Resize frame to new dimensions (if needed)
    im0_resized = cv2.resize(im0, (new_width, new_height))
        
        # Perform object tracking
    tracks = model.track(im0_resized, persist=True, show=False)
        
        # Update counters for each region
    im0_resized = counterJ1.start_counting(im0_resized, tracks)
    im0_resized = counterJ2.start_counting(im0_resized, tracks)
    im0_resized = counterJ3.start_counting(im0_resized, tracks)

    # Draw regions on the image for visualization
    im0_resized = draw_regions(im0_resized, regions)
        
        # Update the last processed time
    
    ''' 
    print(f"Region A: {counterA.class_wise_count}")
    print(f"Region A: {counterA.count_ids}")
    print(f"Region B: {counterB.class_wise_count}")
    print(f"Region C: {counterC.class_wise_count}")
    print(f"Region D: {counterD.class_wise_count}")
    print(f"Region E: {counterE.class_wise_count}")
    print(f"Region F: {counterF.class_wise_count}") 
    '''
    print(f"Region J1: {counterJ1.class_wise_count}")
    print(f"Region J2: {counterJ2.class_wise_count}")
    print(f"Region J3: {counterJ3.class_wise_count}")
        # Show the processed frame in the resizable window
    cv2.imshow('Object Detection', im0_resized)
    
    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()


count_dict = {
    'BC': {cls: 0 for cls in vehicle_classes},
    'BE': {cls: 0 for cls in vehicle_classes},
    'DE': {cls: 0 for cls in vehicle_classes},
    'DA': {cls: 0 for cls in vehicle_classes},
    'FA': {cls: 0 for cls in vehicle_classes},
    'FC': {cls: 0 for cls in vehicle_classes}
}

for count_id in counterJ1.count_ids:
    id=count_id[0]
    if(count_id[2]=='source'):
        vehicle_class_str = vehicle_classes[int(count_id[1])]
        for j2_id in counterJ2.count_ids:
            if(j2_id[0]==id):
                count_dict['BC'][vehicle_class_str]+=1
        for j3_id in counterJ3.count_ids:
            if(j3_id[0]==id):
                count_dict['BE'][vehicle_class_str]+=1
for count_id in counterJ2.count_ids:
    id=count_id[0]
    if(count_id[2]=='source'):
        vehicle_class_str = vehicle_classes[int(count_id[1])]
        for j1_id in counterJ1.count_ids:
            if(j1_id[0]==id):
                count_dict['DA'][vehicle_class_str]+=1
        for j3_id in counterJ3.count_ids:
            if(j3_id[0]==id):
                count_dict['DE'][vehicle_class_str]+=1

for count_id in counterJ3.count_ids:
    id=count_id[0]
    if(count_id[2]=='source'):
        vehicle_class_str = vehicle_classes[int(count_id[1])]
        for j1_id in counterJ1.count_ids:
            if(j1_id[0]==id):
                count_dict['FA'][vehicle_class_str]+=1
        for j2_id in counterJ2.count_ids:
            if(j2_id[0]==id):
                count_dict['FC'][vehicle_class_str]+=1



# Print the results
for pattern, counts in count_dict.items():
    print(f"Turning pattern {pattern}:")
    for vehicle_class, count in counts.items():
        print(f"  {vehicle_class}: {count}")