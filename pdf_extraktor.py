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

# Using pdfminer to get xml template to work with
output_string = StringIO()
with open(args.Eingabedatei, 'rb') as fin:
  extract_text_to_fp(fin, output_string, laparams=LAParams(), output_type='xml', codec=None)

AusgabeDatei = str(args.Eingabedatei).split('/')[-1].split('.')[0] + '.xml'

f = open(AusgabeDatei, "w")
f.write(output_string.getvalue())
f.close()
