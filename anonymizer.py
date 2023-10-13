import util

import xml.etree.ElementTree as ET

def anonymize(file_type, input_tree):
  config_file = ET.parse("doc_config/file_types/" + file_type + ".xml").getroot()
  anonymize_file = ET.parse("doc_config/anonymize_mustermensch.xml").getroot()
  for tag in config_file:
    i0, i1, i2 = util.getIndexe(str(tag.text))
    try:
      input_tree[i0][i1][i2].text = anonymize_file.find(str(tag.tag)).text
    except IndexError:
      # TODO: Fix IndexError wegen Geburtsname
      if file_type == 'Elternzeit':
        print(i0, i1, i2)
      continue

  return util.prettify(input_tree)
