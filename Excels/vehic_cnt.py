import pandas as pd
from datetime import timedelta
from ultralytics import YOLO, solutions
import cv2

# Initialize YOLO model
model = YOLO(r"best.pt")

# Video file path
video_file = r'Video\\Ayyappa_Temple_FIX_1_time_2024-05-14T07_30_02_002.mp4'

# Desired output resolution
new_width = 1000  # New width
new_height = 1000  # New height

# Open video capture
cap = cv2.VideoCapture(video_file)

# Check if video capture is open
assert cap.isOpened(), "Error reading video file"

# Get video frame rate
fps = cap.get(cv2.CAP_PROP_FPS)

# Get actual video resolution
video_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
video_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define region points for object counting
region_points = [(20, 400), (video_width - 20, 404), (video_width - 20, 360), (20, 360)]

# Define vehicle classes
vehicle_classes = ['car', 'bus', 'truck', 'three-wheeler', 'two-wheeler', 'lcv', 'bicycle']

# Dictionary to store cumulative counts
vehicle_counts = {
    'timestamp': [],
    'car_IN': [],
    'car_OUT': [],
    'bus_IN': [],
    'bus_OUT': [],
    'truck_IN': [],
    'truck_OUT': [],
    'three-wheeler_IN': [],
    'three-wheeler_OUT': [],
    'two-wheeler_IN': [],
    'two-wheeler_OUT': [],
    'lcv_IN': [],
    'lcv_OUT': [],
    'bicycle_IN': [],
    'bicycle_OUT': []
}

# Initialize ObjectCounter
counter = solutions.ObjectCounter(
    view_img=False,  # Disable displaying image during processing
    reg_pts=region_points,  # Region of interest points
    classes_names=model.names,  # Class names from the YOLO model
    draw_tracks=True,  # Draw tracking lines for objects
    line_thickness=2  # Thickness of the lines drawn
)

# Create resizable window
cv2.namedWindow('Object Detection', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Object Detection', video_width, video_height)

# Main video processing loop
frame_number = 0
while cap.isOpened():
    # Read a frame
    success, im0 = cap.read()
    
    # If no frame read, break the loop
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    
    # Resize frame to new dimensions (if needed)
    im0_resized = cv2.resize(im0, (new_width, new_height))
    
    # Perform object tracking
    tracks = model.track(im0_resized, persist=True, show=False)
    
    # Start counting objects
    im0_resized = counter.start_counting(im0_resized, tracks)
    
    # Calculate the timestamp for the current frame
    frame_time = timedelta(seconds=frame_number / fps)
    
    # Store current timestamp
    vehicle_counts['timestamp'].append(frame_time)
    
    # Store counts for each vehicle class
    for vehicle_class in vehicle_classes:
        class_counts = counter.class_wise_count.get(vehicle_class, {'IN': 0, 'OUT': 0})
        vehicle_counts[f'{vehicle_class}_IN'].append(class_counts.get('IN', 0))
        vehicle_counts[f'{vehicle_class}_OUT'].append(class_counts.get('OUT', 0))
    
    # Display current counts
    print('In Counts : {}'.format(counter.in_counts))     # display in counts
    print("Out Counts : {}".format(counter.out_counts))   # display out counts
    print("Classwise Counts : {}".format(counter.class_wise_count))   # display total counts
    
    # Add timestamp to the frame
    timestamp_str = str(frame_time)
    cv2.putText(im0_resized, timestamp_str, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
    # Show the processed frame in the resizable window
    cv2.imshow('Object Detection', im0_resized)
    
    # Increment the frame number
    frame_number += 1
    
    # Check for 'q' key press to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close any OpenCV windows
cap.release()
cv2.destroyAllWindows()

# Save data to Excel
df = pd.DataFrame(vehicle_counts)
df.to_excel('vehicle_counts.xlsx', index=False)

print("Data saved to vehicle_counts.xlsx and vehicle_counts.csv")