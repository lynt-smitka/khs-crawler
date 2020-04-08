from . import utils
import camelot
from urllib.parse import urljoin


class web:
    kraj = "Zlínský kraj"

    def crawl(self):
        pocet_okresu = 4
        results = []
        url = "http://www.khszlin.cz/25304-novy-koronavirus-2019-ncov"
        page = utils.get_url(url)
        doc = page.select_one("a.pdf[href*=info_cov19]")["href"]
        filename = utils.download_file(urljoin(url, doc), ".pdf")
        tables = camelot.read_pdf(filename)
        data = tables[0].df.to_dict("records")
        for row in data[1:1+pocet_okresu]:
            results.append({
              "okres": row[0].replace("okres ", ""),
              "kraj": self.kraj,
              "hodnota": int(row[1])
            })
        return results
