import tree_builder
import util
from util import DocumentTypeRecognitionException, MissingConfigException

import xml.etree.ElementTree as ET
from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

def recognize_doc(input_tree):
  # Check for Formulare
  if 'Antrag' in str(input_tree[0][0][0].text):
    file_types = ET.parse('doc_config/file_types.xml').getroot()
    for formular in file_types[0]:
      index0, index1, index2 = util.getIndexe(formular.get('index'))
      if str(formular.text) in str(input_tree[index0][index1][index2].text):
        return formular.tag
    else:
      raise MissingConfigException()
  else:
    if 1 == 1:
      return "Handbuch"
    else:
      raise DocumentTypeRecognitionException()
