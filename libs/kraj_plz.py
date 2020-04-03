from . import utils

from pytesseract import image_to_string
import pytesseract
from PIL import Image

class web:

  kraj= "Plzeňský kraj"
  
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
    img = utils.get_img('http://www.khsplzen.cz/images/KHS/covid19/Plzensky_kraj.jpg')
    
    val = image_to_string(self.num_trick(self.imgcrop(img,297,288)), config='digits').replace('number','').replace(' ','')
    results.append({ 'okres':'Plzeň-město', 'kraj': self.kraj, 'hodnota':val})
    
    val = image_to_string(self.num_trick(self.imgcrop(img,102,235)), config='digits').replace('number','').replace(' ','')
    results.append({ 'okres':'Tachov', 'kraj': self.kraj, 'hodnota':val})
    
    val = image_to_string(self.num_trick(self.imgcrop(img,268,190)), config='digits').replace('number','').replace(' ','')
    results.append({ 'okres':'Plzeň-sever', 'kraj': self.kraj, 'hodnota':val})
    
    val = image_to_string(self.num_trick(self.imgcrop(img,381,260)), config='digits').replace('number','').replace(' ','')
    results.append({ 'okres':'Rokycany', 'kraj': self.kraj, 'hodnota':val})
    
    val = image_to_string(self.num_trick(self.imgcrop(img,124,373)), config='digits').replace('number','').replace(' ','')
    results.append({ 'okres':'Domažlice', 'kraj': self.kraj, 'hodnota':val})
    
    val = image_to_string(self.num_trick(self.imgcrop(img,328,370)), config='digits').replace('number','').replace(' ','')
    results.append({ 'okres':'Plzeň-jih', 'kraj': self.kraj, 'hodnota':val})
    
    val = image_to_string(self.num_trick(self.imgcrop(img,268,494)), config='digits').replace('number','').replace(' ','')
    results.append({ 'okres':'Klatovy', 'kraj': self.kraj, 'hodnota':val})
    return results
