import xml.etree.ElementTree as ET
from xml.dom import minidom

def getIndexe(input_string):
  indexe = [int(index) for index in str(input_string) if index.isdigit()]
  return indexe

def prettify(elem):
  rough_string = ET.tostring(elem, 'utf-8')
  reparsed = minidom.parseString(rough_string)
  return reparsed.toprettyxml(indent="  ")
