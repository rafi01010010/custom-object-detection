import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
#from video import openvid

faces = {
    'model': 'cfg/yolo-face.cfg',
    'load': 'bin/yolo-face_final.weights',
    'threshold': 0.15,
    #'gpu': 0.7
}

cigrates = {
    'model': 'cfg/tiny-yolo-voc-1c.cfg',
    'load': 2000,
    'threshold': 0.15,
    #'gpu': 0.7
}

tfnet = TFNet(faces)
cigrateTf = TFNet(cigrates)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]


capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    stime = time.time()
    ret, frame = capture.read()
    results = tfnet.return_predict(frame)
    if ret:
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence = result['confidence']
            con_percent = confidence*100
            text = '{}: {:.0f}%'.format(label, confidence * 100)
			#if con_percent >= 10:
              #openvid()
            #break
            cv2.rectangle(frame, tl, br, color, 5)
            cv2.putText(frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            # detect cigrates
            cv2.imshow('frame', frame)
            faceArea = frame[result['topleft']['y']:result['bottomright']['y'],result['topleft']['x']:result['bottomright']['x']]
            #cv2.imshow('frame', faceArea)
            cigrateResults = cigrateTf.return_predict(faceArea)
            for c, r in zip(colors,cigrateResults):
                cl = (r['topleft']['x'], r['topleft']['y'])
                cbr = (r['bottomright']['x'], r['bottomright']['y'])
                lab = 'Cigrate'
                conf = r['confidence']
                confPer = conf*100
                cigtext = '{}: {:.0f}%'.format(lab, conf * 100)
                cv2.rectangle(faceArea, cl, cbr, c, 5)
                cv2.putText(faceArea, cigtext, cl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
				
				
        cv2.imshow('frame', frame)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
