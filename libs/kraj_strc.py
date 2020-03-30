from . import utils

class web:

  kraj= "Jihočeský kraj"
  
  def crawl(self):
    results=[]
    soup = utils.get_url('http://www.khsstc.cz/dokumenty/aktualni-situace-ve-vyskytu-koronaviru-ve-stredoceskem-kraji-5723_5723_161_1.html')
    table = soup.select('.vypis p')
    for td in table:
      if td.contents:
        okres = self.mapping(td)
        if okres:
          results.append(okres)

    return results

  def mapping(self, td):

    kraj = self.kraj
    
    if 'Benešovsko' in td.text:
        val = td.text.split()[-1].strip()
        return { 'okres':'Benešov', 'kraj': kraj,  'hodnota':val}
        
    if 'Berounsko' in td.text:
        val = td.text.split()[-1].strip()
        return { 'okres':'Beroun', 'kraj': kraj,  'hodnota':val}

    
    if 'Kladensko' in td.text:
        val = td.text.split()[-1].strip()
        return { 'okres':'Kladno', 'kraj': kraj,  'hodnota':val}

 
    if 'Kolínsko' in td.text:
        val = td.text.split()[-1].strip()
        return { 'okres':'Kolín', 'kraj': kraj,  'hodnota':val}

        
    if 'Kutná Hora' in td.text:
        val = td.text.split()[-1].strip()
        return { 'okres':'Prachatice', 'kraj': kraj,  'hodnota':val}
        
         
    if 'Mělnicko' in td.text:
        val = td.text.split()[-1].strip()
        return { 'okres':'Mělník', 'kraj': kraj,  'hodnota':val}

        
    if 'Mladoboleslavsko' in td.text:
        val = td.text.split()[-1].strip()
        return { 'okres':'Mladá Boleslav', 'kraj': kraj,  'hodnota':val}
        
        
    if 'Nymbursko' in td.text:
        val = td.text.split()[-1].strip()
        return { 'okres':'Nymburk', 'kraj': kraj,  'hodnota':val}

 
    if 'Příbramsko' in td.text:
        val = td.text.split()[-1].strip()
        return { 'okres':'Příbram', 'kraj': kraj,  'hodnota':val}

        
    if 'Rakovnicko' in td.text:
        val = td.text.split()[-1].strip()
        return { 'okres':'Rakovník', 'kraj': kraj,  'hodnota':val}
        
        
         
    if 'Východ' in td.text:
        val = td.text.split()[-1].strip()
        return { 'okres':'Praha-východ', 'kraj': kraj,  'hodnota':val}

        
    if 'Západ' in td.text:
        val = td.text.split()[-1].strip()
        return { 'okres':'Praha-západ', 'kraj': kraj,  'hodnota':val}
        
        

    return False
