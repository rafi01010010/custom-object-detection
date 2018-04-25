import xml.etree.ElementTree
import os


for xmlfile in os.scandir('mi_annotations'):
	fileName = xmlfile.name
	extention = fileName.split('.')
	if extention[1] == 'xml':
		et = xml.etree.ElementTree.parse(xmlfile.path)
		et.find(".//folder").text = "mi_images"
		et.find(".//path").text = "/Users/rafi01010010/Documents/cigarette/darkflow/new_model_data/mi_images/"+extention[0]+".jpg"
		et.write(xmlfile.path)
		print(fileName)