import requests
from bs4 import BeautifulSoup
import PyPDF2
from PIL import Image
import PIL.Image
import hashlib

def get_url(url):
  r = requests.get(url)
  if r.status_code == requests.codes.ok:
    return BeautifulSoup(r.text, 'html.parser')
    
def get_pdf(url, page=0):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
      hash = hashlib.md5(url.encode('utf-8')).hexdigest()
      open('./tmp/%s'%hash, 'wb').write(r.content)
      pdfFileObj = open('./tmp/%s'%hash, 'rb')
      pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
      return pdfReader.getPage(page)
      
def get_img(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
      hash = hashlib.md5(url.encode('utf-8')).hexdigest()
      open('./tmp/%s'%hash, 'wb').write(r.content)
      return Image.open('./tmp/%s'%hash)

