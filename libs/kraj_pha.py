from . import utils
import re

class web:
  kraj= "Praha"
  
  def crawl(self):
    results=[]
    soup = utils.get_url('http://www.hygpraha.cz/obsah/koronavirus_506_1.html')
    link = soup.select_one('.content .vypis-item h3 a[href*=pozitivnich]')
    search = re.search('V Praze ([\d ]+).*hodin', link.text)
    if search:
      val = int(search.groups()[0].replace(" ", "").strip())
      results.append({'okres':'Praha', 'kraj': self.kraj, 'hodnota': val})        
    return results
