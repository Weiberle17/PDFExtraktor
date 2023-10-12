#!./venv/bin/python3

import input_handler
import doc_recognizer

from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

doc_type = doc_recognizer.recognize_doc(input_handler.args.Eingabedatei)

AusgabeDatei = str(input_handler.args.Eingabedatei).split('/')[-1].split('.')[0] + '.xml'

# # Einzelne Textstellen können so angesprochen und verändert werden
# print(root[0][0][0].text)
#
# f = open(AusgabeDatei, "w")
# f.write(prettify(root))
# f.close()
