from . import utils

class web:
  kraj = 'Moravskoslezský kraj'

  def crawl(self):
    khs_url = 'https://koronavirus.msk.cz/'

    okresy = {
      'Bruntál': [
        'Bruntál',
        'Krnov',
        'Rýmařov',
      ],
      'Frýdek-Místek': [
        'Frýdek-Místek',
        'Frýdlant nad Ostravicí',
        'Jablunkov',
        'Třinec',
      ],
      'Karviná': [
        'Bohumín',
        'Český Těšín',
        'Havířov',
        'Karviná',
        'Orlová',
      ],
      'Nový Jičín': [
        'Bílovec',
        'Frenštát pod Radhoštěm',
        'Kopřivnice',
        'Nový Jičín',
        'Odry',
      ],
      'Opava': [
        'Hlučín',
        'Kravaře',
        'Opava',
        'Vítkov',
      ],
      'Ostrava: [
        'Ostrava',
      ]
    }

    html = utils.get_url(khs_url)
    cells = html.select(".article table td")
    pocty_v_obcich = {}
    for i, cell in enumerate(cells):
      if i % 2 == 0:
        pocty_v_obcich[cell.text] = int(cells[i+1].text)
    results = []
    for okres, obce in okresy.items():
      pocet = 0
      for obec in obce:
        pocet = pocet + pocty_v_obcich[obec]
      results.append({'okres': okres, 'kraj': self.kraj, 'hodnota': pocet})

    return results
