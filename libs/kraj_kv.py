from . import utils

#TODO: rozdělit na crawl a mapping

class web:

  kraj= "Karlovarský kraj"
  
  def crawl(self):
    results=[]
    lines = utils.get_pdfminer('http://www.khskv.cz/Koronavir_COVID/Pocet_testovanych_osob_na_COVID19_Karlovarsky_kraj.pdf')
    i=0
    offset = False
    for l in lines:
        i=i+1
        if not offset and not 'DLE OKRESŮ' in l:
            continue
        offset = True
        if 'Karlovy Vary' in l:
            results.append({ 'okres':'Karlovy Vary', 'kraj': self.kraj, 'hodnota':l.split()[-1]})
        if 'Sokolov' in l:
            results.append({ 'okres':'Sokolov', 'kraj': self.kraj, 'hodnota':l.split()[-1]})
        if 'Cheb' in l:
            results.append({ 'okres':'Cheb', 'kraj': self.kraj, 'hodnota':l.split()[-1]})
    return results
