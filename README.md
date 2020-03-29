# khs-crawler

Crawler COVID-19 dat z Krajských hygienických stanic

Prototyp skriptù pro crawling dat jednotlivých KHS. 

*Psáno primitivním stylem, nejsou ošetøeny výjimky atd.*

Použité knihovny:

 - **requests** + **BeautifulSoup** - parsování dat z webù
 - **pdfminer.six** - parsování dat z PDF  
 - **Pillow** - práce s obrázky
 - **pytesseract** - OCR pomocí [Tesseract](https://tesseract-ocr.github.io/)

Motivace: https://twitter.com/marekl/status/1243188839415414784

Informace o zdrojích: [https://www.sablatura.info/covid/hygienicke-stanice/](https://www.sablatura.info/covid/hygienicke-stanice/)

Výstupy: [https://docs.google.com/spreadsheets/d/1FFEDhS6VMWon_AWkJrf8j3XxjZ4J6UI1B2lO3IW-EEc](https://docs.google.com/spreadsheets/d/1FFEDhS6VMWon_AWkJrf8j3XxjZ4J6UI1B2lO3IW-EEc)

## Chybìjící kraje:
- Moravskoslezský kraj - data v obrázkových sloupcových grafech - umístìní hodnoty se mìní... dále je  k dispozici obrázek na homepage, ale sám mám problém ho pøeèíst...



