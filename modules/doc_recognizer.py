from modules import util, exceptions

import xml.etree.ElementTree as ET

def recognize_doc(input_tree):
  # Check for Formulare
  file_types = ET.parse('doc_config/file_types.xml').getroot()
  if 'Antrag' in str(input_tree[0][0][0].text):
    for formular in file_types[0]:
      index0, index1, index2 = util.getIndexe(formular.get('index'))
      if str(formular.text) in str(input_tree[index0][index1][index2].text):
        return (formular.tag, formular.get('textboxes'))
    raise exceptions.MissingConfigException()
  else:
    for handbuch in file_types[1]:
      index0, index1, index2 = util.getIndexe(handbuch.get('index'))
      if str(handbuch.text) in str(input_tree[index0][index1][index2].text):
        return (handbuch.tag, handbuch.get('textboxes'))
    raise exceptions.DocumentTypeRecognitionException()
