from . import utils

class web:
  kraj= 'Ústecký kraj'

  def crawl(self):
    url = 'http://www.khsusti.cz/php/kousky/covid19/pocet_testovanych_osob_na_covid19_ustecky_kraj.pdf'
    pocet_okresu = 7
    results=[]
    lines = [line for line in utils.get_pdfminer(url) if len(line.replace(' ', '')) > 0]
    start_index = None
    distance_to_counts = None
    for i, line in enumerate(lines):
        if line.startswith('okres'):
            start_index = i + 1
            for next_i in range(start_index, len(lines) - i):
                if (lines[next_i][0].isdigit()):
                    distance_to_counts = next_i - i - 1
                    break
            break
    if start_index and distance_to_counts:
        for i in range(start_index, start_index + pocet_okresu):
            name = lines[i].strip().replace('D ín', 'Děčín').replace('Litom ice', 'Litoměřice')
            results.append({'okres': name, 'kraj': self.kraj, 'hodnota': int(lines[i + distance_to_counts].strip())})

    return results

