import os
import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
from generate_xml import write_xml

options = {
    'model': 'cfg/tiny-yolo-voc-2c.cfg',
    'load': 8000,
    'threshold': 0.40,
    #'gpu': 0.7
}

tfnet = TFNet(options)
colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

number = 1

for file in os.scandir('raw_images'):
	filename = file.name
	image = cv2.imread(file.path)
	results = tfnet.return_predict(image)
	tl_list = []
	br_list = []
	object_list = []
	for color, result in zip(colors, results):
		tl = (int(result['topleft']['x']), int(result['topleft']['y']))
		br = (int(result['bottomright']['x']), int(result['bottomright']['y']))
		label = result['label']
		if label == 'cigarette':
			object_list.append(label)
			tl_list.append(tl)
			br_list.append(br)
			cv2.rectangle(image, tl, br, color, 5)
	if len(tl_list) == 0:
		os.rename(file.path,'image_without_cigratee/'+filename)
	else:
		os.rename(file.path,'image_with_cigratee/'+str(number)+'.jpg')
