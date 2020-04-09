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
        val = td.findNext('td').text.split()[0]
        return { 'okres':'České Budějovice', 'kraj': kraj,  'hodnota':int(val)}
        
    if 'Českokrumlovsko' in td.text:
        val = td.findNext('td').text.split()[0]
        return { 'okres':'Český Krumlov', 'kraj': kraj,  'hodnota':int(val)}

    
    if 'Jindřichohradecko' in td.text:
        val = td.findNext('td').text.split()[0]
        return { 'okres':'Jindřichův Hradec', 'kraj': kraj,  'hodnota':int(val)}

 
    if 'Písecko' in td.text:
        val = td.findNext('td').text.split()[0]
        return { 'okres':'Písek', 'kraj': kraj,  'hodnota':int(val)}

        
    if 'Prachaticko' in td.text:
        val = td.findNext('td').text.split()[0]
        return { 'okres':'Prachatice', 'kraj': kraj,  'hodnota':int(val)}
        
        
         
    if 'Strakonicko' in td.text:
        val = td.findNext('td').text.split()[0]
        return { 'okres':'Strakonice', 'kraj': kraj,  'hodnota':int(val)}

        
    if 'Táborsko' in td.text:
        val = td.findNext('td').text.split()[0]
        return { 'okres':'Tábor', 'kraj': kraj,  'hodnota':int(val)}

    return False
