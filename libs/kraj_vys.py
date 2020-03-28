from . import utils

class web:

  kraj= "Kraj Vysočina"
  
  def crawl(self):
    results=[]
    soup = utils.get_url('http://www.khsjih.cz/covid-19.php')
    table = soup.select('table.tabulka_covid tr td')
    for td in table:
      if td.contents:
        okres = self.mapping(td)
        if okres:
          results.append(okres)

    return results

  def mapping(self, td):

    kraj = self.kraj
    
    if 'Jihlava' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Jihlava', 'kraj': kraj,  'hodnota':val}
        
    if 'Brod' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Havlíčkův Brod', 'kraj': kraj,  'hodnota':val}

    
    if 'Pelh' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Pelhřimov', 'kraj': kraj,  'hodnota':val}

 
    if 'okrese T' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Třebíč', 'kraj': kraj,  'hodnota':val}

        
    if 'zavou' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Žďár nad Sázavou', 'kraj': kraj,  'hodnota':val}
        

    return False
