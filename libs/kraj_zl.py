from . import utils
from urllib.parse import urljoin

class web:
  kraj= 'Zlínský kraj'
  
  def crawl(self):
    results = []
    pocet_okresu = 4
    page = utils.get_url('http://www.khszlin.cz/25304-novy-koronavirus-2019-ncov')
    doc = page.select_one('a.pdf[href*=info_cov19]')['href']
    url = urljoin('http://www.khszlin.cz/', doc)
    lines = [line for line in utils.get_pdfminer(url) if len(line.replace(' ', '')) > 0]
    start_index = None
    distance_to_counts = None
    for i, line in enumerate(lines):
      if line.startswith('Počet osob s onemocněním'):
        start_index = i + 1
        for next_i in range(start_index, len(lines) - i):
          if (lines[next_i][0].isdigit()):
            distance_to_counts = next_i - i - 1
            break
        break
    if start_index and distance_to_counts:
      for i in range(start_index, start_index + pocet_okresu):
        name = lines[i].strip().replace('okres ', '')
        results.append({'okres': name, 'kraj': self.kraj, 'hodnota': int(lines[i + distance_to_counts].strip())})

    return results