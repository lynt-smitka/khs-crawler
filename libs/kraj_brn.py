from . import utils
# hodně beta

class web:

  kraj= "Jihomoravský kraj"
  
  def crawl(self):
    results=[]
    page = utils.get_url('http://www.khsbrno.cz/admin/upload/aktuality/?C=M;O=D')
    links = page.select('td a')
    doc=''

    for link in links:
        if "14_" in link['href']:
            doc = link['href']
            break
            
    lines = utils.get_pdfminer('http://www.khsbrno.cz/admin/upload/aktuality/%s'%doc)
       
    
    def calculate_offset(lines):
      i=0
      p1=0
      p2=0
      for line in lines:
        if 'Brno-město' in line:
            p1=i
        if '(první případy ' in line:
            p2=i+2
        i=i+1
      return (p1,p2)

    offset=calculate_offset(lines)

    for i in range(0,7):
      results.append({ 'okres':lines[offset[0]+i].strip(), 'kraj': self.kraj, 'hodnota': lines[offset[0]+9+i]})

    return results