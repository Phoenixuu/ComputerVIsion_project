import cv2 
import mediapipe as mp
import numpy as np

mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

pose = mp_pose.Pose()

cap = cv2.VideoCapture("/home/dunggps/Code_đảo_điên/Human body pose tracking/ComputerVIsion_project/Human body pose tracking/data/student_k-pop_dance (720p).mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
frame_delay = int(500 / fps)

while True:
	ret, img = cap.read()
	img = cv2.resize(img, (600, 400))

	results = pose.process(img)
	# print(results.pose_landmarks)
	mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
							mp_draw.DrawingSpec((255,0,0), 3, 3))
	cv2.imshow("Pose Estimation", img)

	h, w, c = img.shape
	opImg = np.zeros([h, w, c])
	opImg.fill(255)
	mp_draw.draw_landmarks(opImg, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
	cv2.imshow("Extracted Pose", opImg)

	


	if cv2.waitKey(frame_delay) & 0xFF == ord('q'):
		break
