import argparse

# Argument parsing for cli tool
parser = argparse.ArgumentParser(prog='pdf_extraktor', description='Extrahieren von Daten aus PDF-Dokumenten in parsen in xml, oder json')
parser.add_argument('Eingabedatei')
parser.add_argument('Ausgabeformat', choices=['xml', 'json'])
args = parser.parse_args()
