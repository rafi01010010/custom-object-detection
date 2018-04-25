#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 16:57:05 2018

@author: rafi01010010
"""
import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import os
from os import listdir
from os.path import isfile, join
import mimetypes
from shutil import copyfile
from generate_xml import write_xml



options = {
    'model': 'cfg/tiny-yolo-voc-1c.cfg',
    'load': 2000,
    'threshold': 0.2,
    #'gpu': 1.0
}

tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

mypath = 'new_model_data/old_images'
testpath = 'new_model_data/test'
savedir = 'new_model_data/annotations'
tl_list = []
br_list = []
object_list = []

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

number = 1

for name in os.scandir(mypath):
    img = name
    filename = name.name
    extenstion = filename.split('.')
    if(extenstion[1] == 'jpg'):
        print(img.path)
        print(filename)
        image = cv2.imread(img.path)
        results = tfnet.return_predict(image)
        for color, result in zip(colors, results):
            tl = (int(result['topleft']['x']), int(result['topleft']['y']))
            br = (int(result['bottomright']['x']), int(result['bottomright']['y']))
            tl_list.append(tl)
            br_list.append(br)
            label = 'cigarette'
            object_list.append(label)
            confidence = result['confidence']
            cv2.rectangle(image, tl, br, color, 10)
            cv2.imwrite("new_model_data/test_images/"+ str(number) +"-"+ extenstion[0] +".jpg",image)
            copyfile(mypath+"/"+filename, os.path.join("new_model_data/images",str(number)+'.jpg'))
            print("Image number: "+str(number))
            

'''

number = 0

for imgfile in os.scandir('new_model_data/old_images'):
    imagetype = mimetypes.guess_type(imgfile.path)
    if imagetype[0] == "image/jpeg":
        filepath = imgfile.path
        filename = filepath.split('.')
        filenameimage = filename[0].split('/')
        image = cv2.imread(imgfile.path)
        results = tfnet.return_predict(image)
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence = result['confidence']
            text = '{}: {:.0f}%'.format(label, confidence * 100)
            cv2.rectangle(image, tl, br, color, 10)
            cv2.imwrite("new_model_data/test_images/"+ str(number) +"-"+ filenameimage[-1] +".jpg",image)
            copyfile(imgfile.path, os.path.join("new_model_data/images",str(number)+'.jpg'))
            copyfile("new_model_data/old_images/"+filenameimage[-1]+ ".xml", os.path.join("new_model_data/annotations",str(number)+'.xml'))
            print("new_model_data/old_images/"+filenameimage[-1]+ ".xml")
            print(imgfile.path)
            print("Image test:"+str(number))
            number = number+1
            cv2.destroyAllWindows()
            #newimage = image[result['topleft']['y']:result['bottomright']['y'],result['topleft']['x']:result['bottomright']['x']]
        
        #application/xml




    
    #result = tfnet.return_predict(imfile.path)

while True:
    stime = time.time()
    ret, frame = capture.read()
    if ret:
        results = tfnet.return_predict(frame)
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            confidence = result['confidence']
            text = '{}: {:.0f}%'.format(label, confidence * 100)
            frame = cv2.rectangle(frame, tl, br, color, 5)
            frame = cv2.putText(
                frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow('frame', frame)
        print('FPS {:.1f}'.format(1 / (time.time() - stime)))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
'''


