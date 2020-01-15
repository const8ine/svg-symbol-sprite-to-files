import os
import xml.etree.ElementTree as et

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
sourceFolderPath = THIS_FOLDER
exportFolderPath = os.path.join(THIS_FOLDER, 'export/')
sourceFilePath = os.path.join(sourceFolderPath, 'example.svg') # your SVG sprite with symbols pile

tree = et.parse(sourceFilePath)
root = tree.getroot()
symbolsList = list()

def elementToString(element):
    s = element.text or ""
    for sub_element in element:
        s += et.tostring(sub_element)
    s += element.tail
    s = s.replace(':ns0', '').replace('ns0:', '').replace('xmlns="http://www.w3.org/2000/svg"', '')
    return s

for child in root:

	for attribute in child:
		symbolAttributes = child.attrib
		symbolID = symbolAttributes.get('id')
		symbolViewBox = symbolAttributes.get('viewBox')

	childContent = elementToString(child)

	fileContent = '<?xml version="1.0" encoding="UTF-8"?>\n' + '<svg viewBox="' + str(symbolViewBox) + '" version="1.1"\n' + 'xmlns="http://www.w3.org/2000/svg"\n' + 'xmlns:xlink="http://www.w3.org/1999/xlink">\n' + '<g id="' + str(symbolID) + '">' + childContent + '</g>\n</svg>'

	symbolFileName = str(symbolID) + '.svg'
	exportFilePath = os.path.join(exportFolderPath, symbolFileName)
	exportFile = open(exportFilePath ,'w')
	exportFile.write(fileContent)
