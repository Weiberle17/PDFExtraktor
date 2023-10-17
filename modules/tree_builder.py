from io import StringIO
import xml.etree.ElementTree as ET
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

def build_tree(input_file):
# Using pdfminer to get xml template to work with
  output_string = StringIO()
  with open(input_file, 'rb') as fin:
    extract_text_to_fp(fin, output_string, laparams=LAParams(), output_type='xml', codec=None)
    
# Remove first line to allow ET.parse to work properly
  lines = output_string.getvalue().split('\n')
  tree_string = StringIO()
  tree_string.writelines(''.join(lines[1:]))
  tree_string.seek(0)

  tree = ET.parse(tree_string).getroot()
  
  return tree
