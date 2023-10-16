#!./venv/bin/python3

import input_handler
import tree_builder
import doc_recognizer
import anonymizer
import output_handler
from util import FormException, MissingConfigException, DocumentTypeRecognitionException
import sys

try:
  input_tree = tree_builder.build_tree(input_handler.args.Eingabedatei)
  doc_type = doc_recognizer.recognize_doc(input_tree)
  anonymized_tree = anonymizer.anonymize(doc_type, input_tree)
  output_handler.output(input_handler.args.Eingabedatei, anonymized_tree, input_handler.args.Ausgabeformat)
except (MissingConfigException, DocumentTypeRecognitionException, FormException) as e:
  print(f"Error: {e.message}")
  sys.exit(1)
