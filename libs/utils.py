import requests
from bs4 import BeautifulSoup

from PIL import Image
import PIL.Image
import hashlib

from io import StringIO

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser


def get_url(url):
  r = requests.get(url)
  if r.status_code == requests.codes.ok:
    return BeautifulSoup(r.text, 'html.parser')

def download_file(url, ext=""):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
      hash = hashlib.md5(url.encode('utf-8')).hexdigest() + ext
      open('./tmp/%s'%hash, 'wb').write(r.content)
      return './tmp/%s'%hash
    
     
def get_img(url):
      return Image.open(download_file(url))

def get_pdfminer(url, laparams=LAParams()):
    output_string = StringIO()
    with open(download_file(url), 'rb') as in_file:
      parser = PDFParser(in_file)
      doc = PDFDocument(parser)
      rsrcmgr = PDFResourceManager()
      device = TextConverter(rsrcmgr, output_string, laparams=laparams)
      interpreter = PDFPageInterpreter(rsrcmgr, device)
      for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
    
    return output_string.getvalue().split('\n')

    
    
