from . import utils

class web:

  kraj= "Pardubický kraj"
  
  def crawl(self):
    results=[]
    soup = utils.get_url('https://www.khspce.cz/aktualni-situace-ve-vyskytu-koronaviru-v-pardubickem-kraji-2/')
    table = soup.select('.entry-content p')
    for td in table:
      if td.contents:
        okres = self.mapping(td)
        if okres:
          results.append(okres)

    return results

  def mapping(self, td):

    kraj = self.kraj
    
    if 'Pardubice:' in td.text:
        val = td.text.split()[-1]
        return { 'okres':'Pardubice', 'kraj': kraj,  'hodnota':int(val)}
        
    if 'Chrudim' in td.text:
        val = td.text.split()[-1]
        return { 'okres':'Chrudim', 'kraj': kraj,  'hodnota':int(val)}

    
    if 'Svitavy' in td.text:
        val = td.text.split()[-1]
        return { 'okres':'Svitavy', 'kraj': kraj,  'hodnota':int(val)}

 
    if 'Ústí nad Orlicí' in td.text:
        val = td.text.split()[-1]
        return { 'okres':'Ústí nad Orlicí', 'kraj': kraj,  'hodnota':int(val)}


    return False

