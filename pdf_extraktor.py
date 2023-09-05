#!./venv/bin/python3

import argparse
import xml.etree.ElementTree as ET
from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

# Argument parsing for cli tool
parser = argparse.ArgumentParser(prog='pdf_extraktor', description='Extrahieren von Daten aus PDF-Dokumenten in parsen in xml, oder json')
parser.add_argument('Eingabedatei')
parser.add_argument('Ausgabeformat', choices=['xml', 'json'])
args = parser.parse_args()

# Delimiter
dl = "<textline"

# Using pdfminer to get xml template to work with
output_string = StringIO()
with open(args.Eingabedatei, 'rb') as fin:
  extract_text_to_fp(fin, output_string, laparams=LAParams(), output_type='xml', codec=None)

# Parsing string into Sections to turn letters into words
parsed_string = [dl+e for e in output_string.getvalue().split(dl) if e]

root_input = ET.fromstring(output_string.getvalue())
root = ET.Element(root_input.tag)
for pg in root_input:
  page = ET.SubElement(root, pg.tag)
  page.attrib = pg.attrib
  for tb in pg:
    textbox = ET.SubElement(page, tb.tag)
    textbox.attrib = tb.attrib
    text = ''
    for char in tb.iter('text'):
      text += str(char.text)
    textbox.text = text
tree = ET.ElementTree(root)
tree.write('test.xml')

# print(root_input.tag)
# print(root_input.attrib)
# result = ''
# for textbox in root_input.iter('textbox'):
#   result += str(textbox.get('id'))
#   result += ": "
#   result += str(textbox)
#   for char in textbox.iter('text'):
#     result += str(char.text)
# print(result)
