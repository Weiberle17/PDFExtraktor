#!./venv/bin/python3

from modules import input_handler, tree_builder, doc_recognizer, anonymizer, output_handler, exceptions
import sys

try:
  input_tree = tree_builder.build_tree(input_handler.args.Eingabedatei)
  doc_type, expected_textboxes = doc_recognizer.recognize_doc(input_tree)
  anonymized_tree = anonymizer.anonymize(doc_type, expected_textboxes, input_tree)
  output_handler.output(input_handler.args.Eingabedatei, anonymized_tree, input_handler.args.Ausgabeformat)
except (exceptions.MissingConfigException, exceptions.DocumentTypeRecognitionException, exceptions.FormException) as e:
  # Make "Error:" red and the rest the default color
  print(f"\033[91mError:\033[0m {e.message}")
  sys.exit(1)
