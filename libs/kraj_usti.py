from . import utils
from pdfminer.layout import LAParams

class web:
  kraj= 'Ústecký kraj'

  def crawl(self):
    url = 'http://www.khsusti.cz/php/kousky/covid19/pocet_testovanych_osob_na_covid19_ustecky_kraj.pdf'
    pocet_okresu = 7
    results=[]
    laparams=LAParams()
    laparams.boxes_flow=None
    lines = [line for line in utils.get_pdfminer(url, laparams) if len(line.replace(' ', '')) > 0]
    start_index = None
    distance_to_counts = None
    for i, line in enumerate(lines):
        if line.startswith('Děčín'):
            start_index = i
            break
    for i in range(start_index, start_index + pocet_okresu * 3, 3):
        value = int(lines[i+1].strip())
        name = lines[i].strip()
        results.append({'okres': name, 'kraj': self.kraj, 'hodnota': value})

    return results

