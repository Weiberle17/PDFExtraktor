#!./venv/bin/python3

import argparse
import xml.etree.ElementTree as ET
from xml.dom import minidom
from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

# Argument parsing for cli tool
parser = argparse.ArgumentParser(prog='pdf_extraktor', description='Extrahieren von Daten aus PDF-Dokumenten in parsen in xml, oder json')
parser.add_argument('Eingabedatei')
parser.add_argument('Ausgabeformat', choices=['xml', 'json'])
args = parser.parse_args()

# Using pdfminer to get xml template to work with
output_string = StringIO()
with open(args.Eingabedatei, 'rb') as fin:
  extract_text_to_fp(fin, output_string, laparams=LAParams(), output_type='xml', codec=None)

AusgabeDatei = str(args.Eingabedatei).split('/')[-1].split('.')[0] + '.xml'

def prettify(elem):
  rough_string = ET.tostring(elem, 'utf-8')
  reparsed = minidom.parseString(rough_string)
  return reparsed.toprettyxml(indent="  ")

# Remove first line to allow ET.parse to work properly
lines = output_string.getvalue().split('\n')
tree_string = StringIO()
tree_string.writelines(''.join(lines[1:]))
tree_string.seek(0)

tree = ET.parse(tree_string)
root = tree.getroot()

root[0][0][0].text = 'hallo'
print(root[0][0][0].text)

f = open(AusgabeDatei, "w")
f.write(prettify(root))
f.close()
