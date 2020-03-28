from . import utils

class web:

  kraj= "Olomoucký kraj"
  
  def crawl(self):
    results=[]
    soup = utils.get_url('http://www.khsolc.cz/info_verejnost.aspx')
    table = soup.select('table table tr td')
    for td in table:
      if td.contents:
        okres = self.mapping(td)
        if okres:
          results.append(okres)

    return results

  def mapping(self, td):

    kraj = self.kraj
    
    if 'Olomouc' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Olomouc', 'kraj': kraj,  'hodnota':val}
        
    if 'Prostějov' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Prostějov', 'kraj': kraj,  'hodnota':val}

    
    if 'Přerov' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Přerov', 'kraj': kraj,  'hodnota':val}

 
    if 'Šumperk' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Šumperk', 'kraj': kraj,  'hodnota':val}

        
    if 'Jeseník' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Jeseník', 'kraj': kraj,  'hodnota':val}
        
    return False

