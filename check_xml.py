import os
from shutil import copyfile

number = 0
for imfile in os.scandir('mi_annotations'):
	filename = imfile.name
	extenstion = filename.split('.')
	if extenstion[1] == 'xml':
		if os.path.isfile('mi_images/'+extenstion[0]+'.jpg') == False:
			print(filename)
		