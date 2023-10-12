#!./venv/bin/python3

import input_handler
import tree_builder

import xml.etree.ElementTree as ET
from xml.dom import minidom

def prettify(elem):
  rough_string = ET.tostring(elem, 'utf-8')
  reparsed = minidom.parseString(rough_string)
  return reparsed.toprettyxml(indent="  ")

tree = tree_builder.build_tree(input_handler.args.Eingabedatei)

f = open("debug/ausgabe.xml", "w")
f.write(prettify(tree))
f.close()
