from . import utils
import re

class web:

  kraj= "Praha"
  
  def crawl(self):
    results=[]
    soup = utils.get_url('http://www.hygpraha.cz/obsah/koronavirus_506_1.html')
    links = soup.select('.content .vypis-item h3 a')
    for a in links:
        search = re.search('V Praze (\d+).*hodin', a.text)
        if search:
          val = search.groups()[0]
          results.append({ 'okres':'Praha', 'kraj': self.kraj,  'hodnota':val})
          break
        

    return results

