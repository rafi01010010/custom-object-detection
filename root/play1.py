import os
import cv2
from darkflow.net.build import TFNet
import numpy as np
import time



def screenSaver(video=False):
	screensaverFilename = 'screensaver.mp4'
	if video != False:
		if cap:
			cap.release()
			cv2.destroyAllWindows()
		else:
			cv2.destroyAllWindows()
		cap = cv2.VideoCapture(video)
	else:
		cap = cv2.VideoCapture(screensaverFilename)

	
	#cap = cv2.VideoCapture(screensaverFilename)
	#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
	#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
	frame_counter = 0
	while True:
		ret, frame = cap.read()
		if ret:
			#print("Loop fram: "+ str(cap.get(cv2.CAP_PROP_POS_FRAMES)))
			'''if cap.get(cv2.CAP_PROP_POS_FRAMES) == 0:
				print("inside")'''
			cv2.imshow('frame',frame)
			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		else:
			cap = cv2.VideoCapture(screensaverFilename)

	cap.release()
	cv2.destroyAllWindows()


def startWebCapture():
	options = {
	'model': 'cfg/tiny-yolo-voc-2c.cfg',
	'load':8000,
	'threshold': 0.40,
	}
	tfnet = TFNet(options)
	colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]
	capture = cv2.VideoCapture('1.mp4')
	screensaver = cv2.VideoCapture('nosmoking.mp4')
	playVideo = cv2.VideoCapture('screensaver.mp4')
	play = False
	#screensaver.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
	#screensaver.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
	while True:
		stime = time.time()
		ret, frame = capture.read()
		if play == True:
			ret1, frame1 = playVideo.read()
			if ret1:
				cv2.imshow('frame',frame1)
			else:
				play = False
				ret1, frame1 = screensaver.read()
		else:
			ret1, frame1 = screensaver.read()
			if ret1:
				cv2.imshow('frame',frame1)
			else:
				screensaver = cv2.VideoCapture('nosmoking.mp4')
		results = tfnet.return_predict(frame)
		if ret:
			for color, result in zip(colors, results):
				tl = (result['topleft']['x'], result['topleft']['y'])
				br = (result['bottomright']['x'], result['bottomright']['y'])
				label = result['label']
				confidence = result['confidence']
				con_percent = confidence*100
				if label == 'cigarette' and con_percent>40:
					play = True
				else:
					print("Not Found")
				text = '{}: {:.0f}%'.format(label, confidence * 100)
				cv2.rectangle(frame, tl, br, color, 5)
				cv2.putText(frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
		if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		
	#capture.release()
	screensaver.release()
	



if __name__ == "__main__":
	startWebCapture()

	#screenSaver()


