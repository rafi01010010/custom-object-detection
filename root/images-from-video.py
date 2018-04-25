import numpy as np
import cv2

cap = cv2.VideoCapture('1.mp4')
n=1
name = 1
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        n = n+1
        if n%2 == 0:
            cv2.imwrite('raw_images/'+str(name)+'.jpg',frame)
            print(n)
            name = name + 1
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        # & 0xFF is required for a 64-bit system
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
cap.release()
cv2.destroyAllWindows()


'''n = n+1
	if n/10 == 0:
		print(n)
		cv2.imwrite('video_images/'+str(n)+".jpg",frame)'''
