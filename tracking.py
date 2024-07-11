import cv2
import pandas as pd
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO(r"v3_results\kaggle\working\runs\detect\train\weights\best.pt")

# Open the video file
video_path = r'data\Ramaiah_BsStp_JN_FIX_1_time_2024-05-19T07_30_02_011.mp4'
cap = cv2.VideoCapture(video_path)

# Dictionary to hold counts for each vehicle class
vehicle_classes = ['car', 'bus', 'truck', 'three-wheeler', 'two-wheeler', 'lcv', 'bicycle']
vehicle_counts = {cls: 0 for cls in vehicle_classes}

# List to store tracking statistics
tracking_stats = []

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True)

        # Process the results
        for result in results:
            if result is not None:
                # Loop through detected objects
                for obj in result.boxes:
                    # Get the class index
                    class_index = int(obj.cls.item())

                    # Get the class name from the model's names dictionary
                    if class_index in model.names:
                        class_name = model.names[class_index]

                        # Increment the count for the detected class
                        if class_name in vehicle_counts:
                            vehicle_counts[class_name] += 1

                        # Append frame number and class name to tracking stats
                        tracking_stats.append({
                            'frame': int(cap.get(cv2.CAP_PROP_POS_FRAMES)),
                            'class': class_name,
                            'count': vehicle_counts[class_name]
                        })
                    else:
                        print(f"Unknown class index {class_index} detected.")

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("YOLOv8 Tracking", annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()

# Convert tracking stats to a DataFrame
df = pd.DataFrame(tracking_stats)

# Save the DataFrame to an Excel file
output_path = r'tracking_stats.xlsx'
df.to_excel(output_path, index=False)

print(f"Tracking statistics saved to {output_path}")
