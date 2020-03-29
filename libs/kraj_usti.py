from . import utils

#TODO: rozdělit na crawl a mapping

class web:

  kraj= "Ústecký kraj"
  
  def crawl(self):
    results=[]
    lines = utils.get_pdfminer('http://www.khsusti.cz/php/kousky/covid19/pocet_testovanych_osob_na_covid19_ustecky_kraj.pdf')
    i=-17
    for l in lines:
        i=i+1
        if i<10:
            continue
        if 'Děčín' in l:
            results.append({ 'okres':'Děčín', 'kraj': self.kraj, 'hodnota':lines[i].strip()})
        if 'Chomutov' in l:
            results.append({ 'okres':'Chomutov', 'kraj': self.kraj, 'hodnota':lines[i].strip()})
        if 'Most' in l:
            results.append({ 'okres':'Most', 'kraj': self.kraj, 'hodnota':lines[i].strip()})
        if 'Litoměřice' in l:
            results.append({ 'okres':'Litoměřice', 'kraj': self.kraj, 'hodnota':lines[i].strip()})
        if 'Louny' in l:
            results.append({ 'okres':'Louny', 'kraj': self.kraj, 'hodnota':lines[i].strip()} )
        if 'Teplice' in l:
            results.append({ 'okres':'Teplice', 'kraj': self.kraj, 'hodnota':lines[i].strip()})
        if 'Ústí nad Labem' in l:
            results.append({ 'okres':'Ústí nad Labem', 'kraj': self.kraj, 'hodnota':lines[i].strip()})
        

    return results

