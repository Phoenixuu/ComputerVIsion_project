import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
import cvzone
# from pynput.keyboard import Controller 

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon = 1)
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
		["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
		["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]


finalText = ""

def drawALL(img, buttonList):
	
	for button in buttonList:
		x, y = button.pos
		w, h = button.size
		# cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0],
		# 						button.size[0]), 20 ,rt=0)
		cv2.rectangle(img, button.pos, (x + w, y + h), (255,0,255), cv2.FILLED)
		cv2.putText(img, button.text, (x + 20, y + 65),
				cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 4)


		# cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0],
		# 						button.size[0]), 20 ,rt=0)
		cv2.rectangle(img, (1050, 50), (1250, 135), (255, 0, 255), cv2.FILLED)
		cv2.putText(img,"Delete",(1065, 110), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255),3)

		# cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0],
		# 							button.size[0]), 20 ,rt=0)
		cv2.rectangle(img, (1050, 150), (1250, 235), (255, 0, 255), cv2.FILLED)
		cv2.putText(img,"Caplock",(1050, 215), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255),3)
		cv2.circle(img, (1240, 160), 10, (255,255,255), cv2.FILLED)

		cv2.rectangle(img, (1050, 250), (1250, 335), (255, 0, 255), cv2.FILLED)
		cv2.putText(img,"Space",(1070, 310), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,255),3)
		

	return img



class Button():
	def __init__(self, pos, text, size = [85,85]):
		self.pos = pos
		self.text = text
		self.size = size



buttonList = []
for i in range(len(keys)):
	for j, key in enumerate(keys[i]):
		buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

while True:
	success, img = cap.read()
	img = cv2.flip(img,1)
	img = detector.findHands(img)
	lmList, bboxInfo = detector.findPosition(img)
	img = drawALL(img, buttonList)	

	# Hiển thị màu khi ấn vào 
	if lmList:
		for button in buttonList:
			x, y = button.pos
			w, h = button.size

			if x < lmList[8][0] < x+w and y < lmList[8][1] < y+h :
				cv2.rectangle(img, button.pos, (x + w, y + h), (175,0,175), cv2.FILLED)
				cv2.putText(img, button.text, (x + 20, y + 65),
				cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 4)

				l, _ , _ = detector.findDistance(8, 12, img, draw = False)
				print(l)

				## Khi ấn vào 
				if l < 30:
					# keyboard.press(button.text)
					cv2.rectangle(img, button.pos, (x + w, y + h), (0,255,0), cv2.FILLED)
					cv2.putText(img, button.text, (x + 20, y + 65),
					cv2.FONT_HERSHEY_PLAIN, 4, (255,255,255), 4)
					finalText += button.text
					sleep(0.35)

	cv2.rectangle(img, (50,350), (1250,450), (175,0,175), cv2.FILLED)
	cv2.putText(img, finalText, (60, 430),
			cv2.FONT_HERSHEY_PLAIN, 5, (255,255,255), 5)
				



	cv2.imshow("virtual keyboard",img)
	cv2.waitKey(1)