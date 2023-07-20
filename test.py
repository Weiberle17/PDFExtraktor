#!./venv/bin/python3

from io import StringIO

from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

output_string = StringIO()
with open('../PA2/Formulare/Elternzeit Antrag Beschäftigte - Max Mustermann.pdf', 'rb') as fin:
    extract_text_to_fp(fin, output_string, laparams=LAParams(), output_type='xml', codec=None)

print(output_string.getvalue())
