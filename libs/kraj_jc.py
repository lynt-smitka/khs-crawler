from . import utils

class web:

  kraj= "Jihočeský kraj"
  
  def crawl(self):
    results=[]
    soup = utils.get_url('https://www.khscb.cz/')
    table = soup.select('#panel_obsah .cla-text table table tbody tr td')
    for td in table:
      if td.contents:
        okres = self.mapping(td)
        if okres:
          results.append(okres)

    return results

  def mapping(self, td):

    kraj = self.kraj
    
    if 'Českobudějovicko' in td.text:
        val = td.findNext('td').text
        return { 'okres':'České Budějovice', 'kraj': kraj,  'hodnota':val}
        
    if 'Českokrumlovsko' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Český Krumlov', 'kraj': kraj,  'hodnota':val}

    
    if 'Jindřichohradecko' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Jindřichův Hradec', 'kraj': kraj,  'hodnota':val}

 
    if 'Písecko' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Písek', 'kraj': kraj,  'hodnota':val}

        
    if 'Prachaticko' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Prachatice', 'kraj': kraj,  'hodnota':val}
        
        
         
    if 'Strakonicko' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Strakonice', 'kraj': kraj,  'hodnota':val}

        
    if 'Táborsko' in td.text:
        val = td.findNext('td').text
        return { 'okres':'Tábor', 'kraj': kraj,  'hodnota':val}

    return False
