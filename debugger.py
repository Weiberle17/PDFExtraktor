#!./venv/bin/python3

import os
from modules import tree_builder, doc_recognizer, anonymizer, util

import argparse
import xml.etree.ElementTree as ET
from xml.dom import minidom

parser = argparse.ArgumentParser(prog='pdf_extraktor', description='Debug module for pdf_extraktor')
parser.add_argument('Eingabedatei')
parser.add_argument('-dt', '--doc_type', action='store_true', help='Display recognized doc type')
parser.add_argument('-re', '--raw_extraction', action='store_true', help='Get raw extraction - written to debug/ausgabe.xml')
parser.add_argument('-a', '--anonymize', action='store_true', help='Get anonymized data - written to debug/ausgabe.xml')
args = parser.parse_args()

if not os.path.exists("debug/"):
  os.makedirs("debug/")

if args.doc_type:
  tree = tree_builder.build_tree(args.Eingabedatei)
  print(doc_recognizer.recognize_doc(tree))

if args.raw_extraction:
  tree = tree_builder.build_tree(args.Eingabedatei)
  f = open("debug/ausgabe.xml", "w")
  f.write(util.prettify(tree))
  print("Written to debug/ausgabe.xml")
  f.close()

if args.anonymize:
  tree = tree_builder.build_tree(args.Eingabedatei)
  doc_type = doc_recognizer.recognize_doc(tree)
  anonymized = anonymizer.anonymize(doc_type, tree)
  f = open("debug/ausgabe.xml", "w")
  f.write(anonymized)
  print("Written to debug/ausgabe.xml")
  f.close()
