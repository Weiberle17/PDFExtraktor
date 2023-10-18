from modules import util, exceptions

import xml.etree.ElementTree as ET
import sys

def anonymize(file_type, expected_textboxes, input_tree):
  try:
    config_file = ET.parse("doc_config/file_types/" + file_type + ".xml").getroot()
    anonymize_file = ET.parse("doc_config/anonymize_mustermensch.xml").getroot()
    actual_textboxes = 0
    for page in input_tree:
      actual_textboxes += len(page.findall('textbox'))
    if int(expected_textboxes) != int(actual_textboxes):
      raise exceptions.FormException
    for tag in config_file:
      i0, i1, i2 = util.getIndexe(str(tag.text))
      try:
        input_tree[i0][i1][i2].text = anonymize_file.find(str(tag.tag)).text
      except IndexError:
        raise exceptions.FormException()

    return util.prettify(input_tree)
  except FileNotFoundError:
    raise exceptions.MissingConfigException
