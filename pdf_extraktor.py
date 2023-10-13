#!./venv/bin/python3

import input_handler
import tree_builder
import doc_recognizer
import anonymizer
import output_handler

from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

input_tree = tree_builder.build_tree(input_handler.args.Eingabedatei)
doc_type = doc_recognizer.recognize_doc(input_tree)
anonymized_tree = anonymizer.anonymize(doc_type, input_tree)
output_handler.output(input_handler.args.Eingabedatei, anonymized_tree)

# # Einzelne Textstellen können so angesprochen und verändert werden
# print(root[0][0][0].text)
#
# f = open(AusgabeDatei, "w")
# f.write(prettify(root))
# f.close()
