from . import utils
from urllib.parse import urljoin
from pdfminer.layout import LAParams


class web:
    kraj = "Jihomoravský kraj"

    def crawl(self):
        pocet_okresu = 7
        results = []
        url = "http://www.khsbrno.cz/admin/upload/aktuality/?C=M;O=D"
        page = utils.get_url(url)
        doc = page.select_one("a[href$=pdf]")["href"]
        lines = [line for line in utils.get_pdfminer(
            urljoin(url, doc)) if len(line.replace(" ", "")) > 0]
        start_index = None
        distance_to_counts = None
        for i, line in enumerate(lines):
            if line.startswith("Počet případů"):
                start_index = i + 1
                break
        for i, line in enumerate(lines):
            if line.startswith("Okres"):
                distance_to_counts = i - start_index + 1
                break
        for i in range(start_index, start_index + pocet_okresu):
            value = int(lines[i].strip())
            name = lines[i+distance_to_counts].strip()
            results.append(
                {"okres": name, "kraj": self.kraj, "hodnota": value})

        return results
