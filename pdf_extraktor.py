#!./venv/bin/python3

from pypdf import PdfReader

reader = PdfReader("../PA2/Formulare/Elternzeit Antrag Beschäftigte - Max Mustermann.pdf")

for page in reader.pages:
  print(page.extract_text())
