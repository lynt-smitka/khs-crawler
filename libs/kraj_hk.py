from . import utils

class web:

  kraj= "Královéhradecký kraj"
  
  def crawl(self):
    results=[]
    soup = utils.get_url('http://www.khshk.cz/news.php')
    tds = soup.findAll('table')[0].findAll('td')
    i = 0
    for td in tds:
      if td.contents:
        okres = self.mapping(td, tds, i)
        if okres:
          results.append(okres)
        
      i=i+1
    return results

  def mapping(self, td, tds, i):

    kraj = self.kraj

    if 'Hr.Králové' in td.text:
        val = tds[i+8].text.strip()
        return { 'okres':'Hradec Králové', 'kraj': kraj,  'hodnota':int(val)}
        
    if 'Jičín' in td.text:
        val = tds[i+8].text.strip()
        return { 'okres':'Jičín', 'kraj': kraj,  'hodnota':int(val)}

    
    if 'Náchod' in td.text:
        val = tds[i+8].text.strip()
        return { 'okres':'Náchod', 'kraj': kraj,  'hodnota':int(val)}

 
    if 'Rychnov' in td.text:
        val = tds[i+8].text.strip()
        return { 'okres':'Rychnov nad Kněžnou', 'kraj': kraj,  'hodnota':int(val)}

        
    if 'Trutnov' in td.text:
        val = tds[i+8].text.strip()
        return { 'okres':'Trutnov', 'kraj': kraj,  'hodnota':int(val)}
        

    return False


