import os
from shutil import copyfile

number = 0
for imfile in os.scandir('old_images'):
	filename = imfile.name
	extenstion = filename.split('.')
	if extenstion[1] == 'xml':
		if os.path.isfile(imfile.path):
			number = number + 1
			print (number)
			copyfile('old_images/'+extenstion[0]+'.jpg','images/'+str(number)+'.jpg')
			copyfile('old_images/'+extenstion[0]+'.xml','annotations/'+str(number)+'.xml')

