import requests
from bs4 import BeautifulSoup
import PyPDF2
from PIL import Image
import PIL.Image
import hashlib
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBox, LTTextLine, LTImage, LTFigure,LTTextBoxHorizontal






def parse_lt_objs (lt_objs, page_number = 0, images_folder = None, text=[]):
        """Iterate through the list of LT* objects and capture the text or image data contained in each"""
        text_content = [] 

        page_text = {} # k=(x0, x1) of the bbox, v=list of text strings within that bbox width (physical column)
        for lt_obj in lt_objs:
            #print(lt_obj)
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine) or isinstance(lt_obj, LTTextBoxHorizontal):
                # text, so arrange is logically based on its column width
                page_text = update_page_text_hash(page_text, lt_obj)

        for k, v in sorted([(key,value) for (key,value) in page_text.items()]):
            # sort the page_text hash by the keys (x0,x1 values of the bbox),
            # which produces a top-down, left-to-right sequence of related columns
            text_content.append('\n'.join(v))

        return '\n'.join(text_content)

def update_page_text_hash (h, lt_obj, pct=0.2):
        """Use the bbox x0,x1 values within pct% to produce lists of associated text within the hash"""
        x0 = lt_obj.bbox[0]
        x1 = lt_obj.bbox[2]
        key_found = False
        for k, v in h.items():
            hash_x0 = k[0]
            if x0 >= (hash_x0 * (1.0-pct)) and (hash_x0 * (1.0+pct)) >= x0:
                hash_x1 = k[1]
                if x1 >= (hash_x1 * (1.0-pct)) and (hash_x1 * (1.0+pct)) >= x1:
                    # the text inside this LT* object was positioned at the same
                    # width as a prior series of text, so it belongs together
                    key_found = True
                    v.append(to_bytestring(lt_obj.get_text()))
                    h[k] = v
        if not key_found:
            # the text, based on width, is a new series,
            # so it gets its own series (entry in the hash)
            h[(x0,x1)] = [to_bytestring(lt_obj.get_text())]
        return h

def to_bytestring (s, enc='utf-8'):
        """Convert the given unicode string to a bytestring, using the standard encoding,
        unless it's already a bytestring"""
        if s:
            if isinstance(s, str):
                return s
            else:
                return s.encode(enc) 



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

def get_pdfminer(url):
    # funkce pro pdfminer jsem si pùjèil z http://denis.papathanasiou.org/archive/2010.08.04.post.pdf
    fp = open(download_file(url), 'rb')
    parser = PDFParser(fp)
    document = PDFDocument(parser)
    layout = None
    laparams = LAParams()
    rsrcmgr = PDFResourceManager()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
        layout = device.get_result()
    
    return parse_lt_objs(layout).split('\n')
    
    
