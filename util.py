import xml.etree.ElementTree as ET
from xml.dom import minidom
import re

# TODO: Create custom exceptions

def getIndexe(input_string):
  indexe = [int(match.group()) for match in re.finditer(r'\d+', input_string)]
  return indexe

def prettify(elem):
  rough_string = ET.tostring(elem, 'utf-8')
  reparsed = minidom.parseString(rough_string)
  return reparsed.toprettyxml(indent="  ")
