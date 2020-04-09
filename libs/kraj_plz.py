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
        if px > (100, 255):
          cropped.putpixel((px_x, px_y), (255, 255))
        if px < (100, 255):
          cropped.putpixel((px_x, px_y), (0, 255))
    return cropped
  
  def crawl(self):
    tsconfig='--psm 7 digits'
    results=[]
    img = utils.get_img('http://www.khsplzen.cz/images/KHS/covid19/Plzensky_kraj.jpg')
    
    val = int(image_to_string(self.imgcrop(img,294,285), config=tsconfig))
    results.append({ 'okres':'Plzeň-město', 'kraj': self.kraj, 'hodnota':val})
    
    val = int(image_to_string(self.imgcrop(img,100,234), config=tsconfig))
    results.append({ 'okres':'Tachov', 'kraj': self.kraj, 'hodnota':val})
    
    val = int(image_to_string(self.imgcrop(img,262,187), config=tsconfig))
    results.append({ 'okres':'Plzeň-sever', 'kraj': self.kraj, 'hodnota':val})
    
    val = int(image_to_string(self.imgcrop(img,375,257), config=tsconfig))
    results.append({ 'okres':'Rokycany', 'kraj': self.kraj, 'hodnota':val})
    
    val = int(image_to_string(self.imgcrop(img,118,370), config=tsconfig))
    results.append({ 'okres':'Domažlice', 'kraj': self.kraj, 'hodnota':val})
    
    val = int(image_to_string(self.imgcrop(img,322,368), config=tsconfig))
    results.append({ 'okres':'Plzeň-jih', 'kraj': self.kraj, 'hodnota':val})
    
    val = int(image_to_string(self.imgcrop(img,265,492), config=tsconfig))
    results.append({ 'okres':'Klatovy', 'kraj': self.kraj, 'hodnota':val})

    return results
