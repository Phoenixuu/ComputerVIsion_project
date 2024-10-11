# import cv2 

# cv2.VideoCapture("/home/dunggps/Code_đảo_điên/Human body pose tracking/ComputerVIsion_project/Human body pose tracking/data/Dance.mp4")

# while True:
# 	ret, img = cap.read()

# 	cv2.imshow("Pose Estimation", img)
# 	cv2.waitKey(1)

import cv2

# Initialize video capture
cap = cv2.VideoCapture("/home/dunggps/Code_đảo_điên/Human body pose tracking/ComputerVIsion_project/Human body pose tracking/data/student_k-pop_dance (720p).mp4")

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)

print(f"Frame Width: {frame_width}, Frame Height: {frame_height}")
print(f"Total Frames: {frame_count}, FPS: {fps}")

# Check if the video capture object was successfully initialized
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Calculate delay between frames to match the actual FPS of the video
frame_delay = int(1000 / fps)  # Delay in milliseconds

# Loop to read and display frames
while True:
    ret, img = cap.read()

    # Break the loop if the video ends or frame is not captured
    if not ret:
        print("End of video or cannot fetch the frame.")
        break

    # Show the current frame
    cv2.imshow("Pose Estimation", img)

    # Wait for x millisecond and break the loop if 'q' is pressed
    if cv2.waitKey(frame_delay) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
