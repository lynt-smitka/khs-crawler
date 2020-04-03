from . import utils

from pytesseract import image_to_string
import pytesseract
from PIL import Image

class web:

  kraj= "Plzeňský kraj"
  
  def imgcrop(self,img,x,y,w=50,h=35):
    cropped = img.crop((x,y,x+w,y+h)).convert('LA')
    for px_x in range(0, w):
      for px_y in range(0, h):
        px = cropped.getpixel((px_x, px_y))
        if px > (200, 255):
          cropped.putpixel((px_x, px_y), (255, 255))
    return cropped
  
  def crawl(self):
    results=[]
    img = utils.get_img('http://www.khsplzen.cz/images/KHS/covid19/Plzensky_kraj.jpg')
    
    val = image_to_string(self.imgcrop(img,294,285), config='digits')
    results.append({ 'okres':'Plzeň-město', 'kraj': self.kraj, 'hodnota':val})
    
    val = image_to_string(self.imgcrop(img,100,234), config='digits')
    results.append({ 'okres':'Tachov', 'kraj': self.kraj, 'hodnota':val})
    
    val = image_to_string(self.imgcrop(img,262,187), config='digits')
    results.append({ 'okres':'Plzeň-sever', 'kraj': self.kraj, 'hodnota':val})
    
    val = image_to_string(self.imgcrop(img,375,257), config='digits')
    results.append({ 'okres':'Rokycany', 'kraj': self.kraj, 'hodnota':val})
    
    val = image_to_string(self.imgcrop(img,118,370), config='digits')
    results.append({ 'okres':'Domažlice', 'kraj': self.kraj, 'hodnota':val})
    
    val = image_to_string(self.imgcrop(img,322,368), config='digits')
    results.append({ 'okres':'Plzeň-jih', 'kraj': self.kraj, 'hodnota':val})
    
    val = image_to_string(self.imgcrop(img,265,492), config='digits')
    results.append({ 'okres':'Klatovy', 'kraj': self.kraj, 'hodnota':val})

    return results
