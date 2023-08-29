#!./venv/bin/python3

import sys
import argparse
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

for section in parsed_string:
  print("Section:")
  print(section)
  print()
