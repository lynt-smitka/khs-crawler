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

def download_file(url):
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
      hash = hashlib.md5(url.encode('utf-8')).hexdigest()
      open('./tmp/%s'%hash, 'wb').write(r.content)
      return './tmp/%s'%hash
    
def get_pdf(url, page=0):
      pdfFileObj = open(download_file(url), 'rb')
      pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
      return pdfReader.getPage(page)
      
def get_img(url):
      return Image.open(download_file(url))

