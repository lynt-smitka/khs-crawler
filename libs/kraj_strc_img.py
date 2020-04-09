from . import utils

from pytesseract import image_to_string
import pytesseract
from PIL import Image

class web:

  kraj= "Středočeský kraj"
  
  def imgcrop(self,img,x,y,w=44,h=32):
    return img.crop((x,y,x+w,y+h))  
  
  def num_trick(self,img):
    num_img = Image.open('./files/number.jpg')
    new_img = Image.new('RGB', (144, 32))
    new_img.paste(num_img, (0,0))
    new_img.paste(img, (100,0))
    return new_img
  
  def crawl(self):
    results=[]
    img = utils.get_img('http://www.khsstc.cz/Admin/_upload/images/1/COVID%2027_3.jpg')
    
    val = image_to_string(self.num_trick(self.imgcrop(img,327,366))).replace('number','').replace(' ','')
    results.append({ 'okres':'Rakovník', 'kraj': self.kraj, 'hodnota':int(val)})
    
    val = image_to_string(self.num_trick(self.imgcrop(img,472,260))).replace('number','').replace(' ','')
    results.append({ 'okres':'Kladno', 'kraj': self.kraj, 'hodnota':int(val)})
    
    val = image_to_string(self.num_trick(self.imgcrop(img,630,208))).replace('number','').replace(' ','')
    results.append({ 'okres':'Mělník', 'kraj': self.kraj, 'hodnota':int(val)})
    
    val = image_to_string(self.num_trick(self.imgcrop(img,819,171))).replace('number','').replace(' ','')
    results.append({ 'okres':'Mladá Boleslav', 'kraj': self.kraj, 'hodnota':int(val)})
    
    val = image_to_string(self.num_trick(self.imgcrop(img,878,312))).replace('number','').replace(' ','')
    results.append({ 'okres':'Nymburk', 'kraj': self.kraj, 'hodnota':int(val)})
    
    val = image_to_string(self.num_trick(self.imgcrop(img,895,411))).replace('number','').replace(' ','')
    results.append({ 'okres':'Kolín', 'kraj': self.kraj, 'hodnota':int(val)})
    
    val = image_to_string(self.num_trick(self.imgcrop(img,950,507))).replace('number','').replace(' ','')
    results.append({ 'okres':'Kutná Hora', 'kraj': self.kraj, 'hodnota':int(val)})
    
    val = image_to_string(self.num_trick(self.imgcrop(img,790,614))).replace('number','').replace(' ','')
    results.append({ 'okres':'Benešov', 'kraj': self.kraj, 'hodnota':int(val)})
    
    val = image_to_string(self.num_trick(self.imgcrop(img,495,626))).replace('number','').replace(' ','')
    results.append({ 'okres':'Příbram', 'kraj': self.kraj, 'hodnota':int(val)})    
    
    val = image_to_string(self.num_trick(self.imgcrop(img,431,483))).replace('number','').replace(' ','')
    results.append({ 'okres':'Beroun', 'kraj': self.kraj, 'hodnota':int(val)})

    val = image_to_string(self.num_trick(self.imgcrop(img,746,438))).replace('number','').replace(' ','')
    results.append({ 'okres':'Praha-východ', 'kraj': self.kraj, 'hodnota':int(val)})
    
    val = image_to_string(self.num_trick(self.imgcrop(img,588,482))).replace('number','').replace(' ','')
    results.append({ 'okres':'Praha-západ', 'kraj': self.kraj, 'hodnota':int(val)})

    
    return results
