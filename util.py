import xml.etree.ElementTree as ET
from xml.dom import minidom
import re

class MissingConfigException(Exception):
  def __init__(self) -> None:
    self.message = "Keine Konfiguration für dieses Formular gefunden"
    super().__init__(self.message)

class DocumentTypeRecognitionException(Exception):
  def __init__(self) -> None:
    self.message = "Dokumentart nicht erkannt"
    super().__init__(self.message)

class FormException(Exception):
  def __init__(self) -> None:
    self.message = "Das Formular hat eine andere Stuktur als erwartet"
    super().__init__(self.message)

def getIndexe(input_string):
  indexe = [int(match.group()) for match in re.finditer(r'\d+', input_string)]
  return indexe

def prettify(elem):
  rough_string = ET.tostring(elem, 'utf-8')
  reparsed = minidom.parseString(rough_string)
  return reparsed.toprettyxml(indent="  ")
