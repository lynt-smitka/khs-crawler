from . import utils

#TODO: rozdělit na crawl a mapping

class web:

  kraj= "Ústecký kraj"
  
  def crawl(self):
    results=[]
    page = utils.get_pdf('http://www.khsusti.cz/php/kousky/covid19/pocet_testovanych_osob_na_covid19_ustecky_kraj.pdf')
    lines=page.extractText().split('\n')
    i=0
    for l in lines:
        i=i+1
        if i<10:
            continue
        if 'ín' in l:
            results.append({ 'okres':'Děčín', 'kraj': self.kraj, 'hodnota':lines[i]})
        if 'Chomutov' in l:
            results.append({ 'okres':'Chomutov', 'kraj': self.kraj, 'hodnota':lines[i]})
        if 'Most' in l:
            results.append({ 'okres':'Most', 'kraj': self.kraj, 'hodnota':lines[i]})
        if 'ice' in l:
            results.append({ 'okres':'Litoměřice', 'kraj': self.kraj, 'hodnota':lines[i]})
        if 'Louny' in l:
            results.append({ 'okres':'Louny', 'kraj': self.kraj, 'hodnota':lines[i]} )
        if 'Teplice' in l:
            results.append({ 'okres':'Teplice', 'kraj': self.kraj, 'hodnota':lines[i]})
        if 'Ústí nad Labem' in l:
            results.append({ 'okres':'Ústí nad Labem', 'kraj': self.kraj, 'hodnota':lines[i]})

    return results

