from . import utils
import camelot
from urllib.parse import urljoin


class web:
    kraj = "Jihomoravský kraj"

    def crawl(self):
        pocet_okresu = 7
        results = []
        url = "http://www.khsbrno.cz/admin/upload/aktuality/?C=M;O=D"
        page = utils.get_url(url)
        doc = page.select_one("a[href$=pdf]")["href"]
        filename = utils.download_file(urljoin(url, doc), ".pdf")
        tables = camelot.read_pdf(filename)
        data = tables[0].df.to_dict("records")
        for row in data[1:1+pocet_okresu]:
            results.append({
              "okres": row[0],
              "kraj": self.kraj,
              "hodnota": int(row[1])
            })
        return results
