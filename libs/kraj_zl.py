from . import utils
# hodně beta

class web:

  kraj= "Zlínksý kraj"
  
  def crawl(self):
    results=[]
    page = utils.get_url('http://www.khszlin.cz/')
    links = page.select('a.pdf')
    doc=''

    for link in links:
        if "info_cov19" in link['href']:
            doc = link['href']
            break
            
    lines = utils.get_pdfminer('http://www.khszlin.cz%s'%doc)
    
    def calculate_offset(lines):
      i=0
      p1=0
      p2=0
      for line in lines:
        if 'okres Kroměříž' in line:
            p1=i
        if 'Zdroj: KHS ZK' in line:
            p2=i+17
        i=i+1
      return (p1,p2)

    offset=calculate_offset(lines)

    mesta= ['Kroměříž', 'Uherské Hradiště', 'Vsetín','Zlín' ]
    offsets = [0,2,4,6]
    for i in range(0,4):
      results.append({ 'okres':mesta[i], 'kraj': self.kraj, 'hodnota': lines[offset[1]+offsets[i]]})
    return results