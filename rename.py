import os
from shutil import copyfile

imdir = 'v_images'
if not os.path.isdir(imdir):
    os.mkdir(imdir)

folders = [folder for folder in os.listdir('.') if 'video_images' in folder]
number = 2007
for imfile in os.scandir('video_images'):
	filename = imfile.name
	extention = filename.split('.')
	if extention[1] == 'jpg':
		number = number + 1
		copyfile(imfile.path,'v_images/'+str(number)+ ".jpg")
