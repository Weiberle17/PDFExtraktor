#!./venv/bin/python3

import json
import xmltodict
import os

def output(file_name, input_tree, output_type):
  AusgabeDatei = ""
  output = ""
  if not os.path.exists("output/"):
    os.makedirs("output/")
  if output_type == "xml":
    AusgabeDatei = "output/" + file_name.split(os.sep)[-1].split('.')[0] + '.xml'
    output = input_tree
  elif output_type == "json":
    AusgabeDatei = "output/" + file_name.split(os.sep)[-1].split('.')[0] + '.json'
    output = json.dumps(xmltodict.parse(input_tree), indent=2, ensure_ascii=False)
  f = open(AusgabeDatei, "w", encoding="utf-8")
  f.write(str(output))
  f.close()
  print("Datei erfolgreich erstellt")
