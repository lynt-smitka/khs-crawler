from . import utils

class web:

  kraj= "Liberecký kraj"
  
  def crawl(self):
    results=[]
    soup = utils.get_url('https://www.khslbc.cz/khs_informace_covid-19/')
    table = soup.select('table')[0].select('tr td')
    for td in table:
      if td.contents:
        okres = self.mapping(td)
        if okres:
          results.append(okres)

    return results

  def mapping(self, td):

    kraj = self.kraj
    
    if 'okrese Česká Lípa' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Česká Lípa', 'kraj': kraj,  'hodnota':int(val)}
        
    if 'okrese Jablonec nad Nisou' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Jablonec nad Nisou', 'kraj': kraj,  'hodnota':int(val)}

    
    if 'okrese Liberec' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Liberec', 'kraj': kraj,  'hodnota':int(val)}

 
    if 'okrese Semily' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Semily', 'kraj': kraj,  'hodnota':int(val)}

    return False


