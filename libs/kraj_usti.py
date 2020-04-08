from .utils import download_file
import camelot


class web:
    kraj = "Ústecký kraj"

    def crawl(self):
        pocet_okresu = 7
        results = []
        url = "http://www.khsusti.cz/php/kousky/covid19/pocet_testovanych_osob_na_covid19_ustecky_kraj.pdf"
        filename = download_file(url, ".pdf")
        tables = camelot.read_pdf(filename)
        data = tables[1].df.to_dict("records")
        for row in data[1:1+pocet_okresu]:
            results.append({
              "okres": row[0],
              "kraj": self.kraj,
              "hodnota": int(row[1])
            })
        return results
