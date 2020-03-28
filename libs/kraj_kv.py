from . import utils

#TODO: rozdělit na crawl a mapping
# 28.3. KHS odstanila z PDF informaci o jednitlivých okrsech...
class web:

  kraj= "Karlovarský kraj"
  
  def crawl(self):
    results=[]
    page = utils.get_pdf('http://www.khskv.cz/Koronavir_COVID/Pocet_testovanych_osob_na_COVID19_Karlovarsky_kraj.pdf')
    lines = page.extractText().split('\n')
    lines = ' '.join(lines).split()
    i=0
    for l in lines:
        print(l)
        i=i+1
        if i<10:
            continue
        if 'Sokolov' in l:
        # řetězec karlovy vary je někde posunutý, najdeme tedy Sokolov a jdeme zpět
            results.append({ 'okres':'Karlovy Vary', 'kraj': self.kraj, 'hodnota':lines[i-2]})
        if 'Sokolov' in l:
            results.append({ 'okres':'Sokolov', 'kraj': self.kraj, 'hodnota':lines[i]})
        if 'Cheb' in l:
            results.append({ 'okres':'Cheb', 'kraj': self.kraj, 'hodnota':lines[i]})
    return results
