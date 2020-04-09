import requests

class web:
  kraj = 'Středočeský kraj'
  
  def crawl(self):
    results= []
    url = 'https://services7.arcgis.com/6U6Ps5FLizN0Qujz/ArcGIS/rest/services/Počet_onemocnění_COVID19_ve_Středočeském_kraji/FeatureServer/0/query'
    params = {
      'where': '1=1',
      'outFields': 'nazev,PocetPripadu',
      'returnGeometry': False,
      'f': 'json'
    }
    features = requests.get(url, params=params).json()['features']
    for feature in features:
      results.append({
        'okres': feature['attributes']['nazev'],
        'kraj': self.kraj,
        'hodnota': int(feature['attributes']['PocetPripadu'])
      })
    return results