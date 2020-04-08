# khs-crawler

Tento *khs-crawler* zpracovává data z Krajských hygienických stanic o počtu identifikovaných nakažených osobách virem způsobujícím onemocnění COVID-19 a generuje je do Google Tabulky. 

## Data

Výstupy dat jsou dostupné v [Google Tabulkách, list Test Crawl](https://docs.google.com/spreadsheets/d/1FFEDhS6VMWon_AWkJrf8j3XxjZ4J6UI1B2lO3IW-EEc/edit#gid=84317159)

    https://docs.google.com/spreadsheets/d/1FFEDhS6VMWon_AWkJrf8j3XxjZ4J6UI1B2lO3IW-EEc/edit#gid=84317159

## Potenciální problémy ⚠️
- Středočeský kraj [publikuje svá data nekonzistentně - více viz issues#4](https://github.com/lynt-smitka/khs-crawler/issues/4)
- Některé kraje nepublikují svá data ve strojově snadno čitelném formátu, zejména u těchto může nacházet k nestabilitě dat, více viz níže sekce [Zdroje dat](#Zdroje-dat)

## Technické informace
V této fázi vývoje se jedná stále o prototyp skriptů pro crawling dat jednotlivých KHS. Pracujte s ním opatrně, kód je psán primitivním stylem. Kupříkladu nejsou ošetřeny výjimky a podobně.

### Použité knihovny

 - **requests** + **BeautifulSoup** - parsování dat z webů
 - **pdfminer.six** a **camelot-py** - parsování dat z PDF  
 - **Pillow** - práce s obrázky
 - **pytesseract** - OCR pomocí [Tesseract](https://tesseract-ocr.github.io/)

### Proč tento crawler vznikl

Motivací byl status Marka Lutoňského o [neexistenci jednotných dat](https://twitter.com/marekl/status/1243188839415414784) pro COVID-19 u jednotlivých okresů, kde každá krajská hygienická stanice reportuje data svým vlastním způsobem.

### Kam se generují výstupy
Výstupy lze nalézt v [Google Tabulkách, listu Test Crawl](https://docs.google.com/spreadsheets/d/1FFEDhS6VMWon_AWkJrf8j3XxjZ4J6UI1B2lO3IW-EEc/edit#gid=84317159)

    https://docs.google.com/spreadsheets/d/1FFEDhS6VMWon_AWkJrf8j3XxjZ4J6UI1B2lO3IW-EEc/edit#gid=84317159

### Zdroje dat
Detailnější informace o zdrojích dat, spolu s tím, které objekty DOM se scrapují, lze nalézt na: [sablatura.info/covid/hygienicke-stanice](https://www.sablatura.info/covid/hygienicke-stanice/)

| Kraj | Formát dat | Url |
|---|---|---|
| Jihočeský | HTML tabulka | https://www.khscb.cz/ |
| Jihomoravský | PDF ⚠️ | http://www.khsbrno.cz/admin/upload/aktuality/?C=M;O=D |
| Karlovarský | PDF ⚠️ | http://www.khskv.cz/Koronavir_COVID/Pocet_testovanych_osob_na_COVID19_Karlovarsky_kraj.pdf |
| Vysočina | HTML tabulka | http://www.khsjih.cz/covid-19.php |
| Královéhradecký | HTML tabulka | http://www.khshk.cz/news.php |
| Liberecký | HTML tabulka | https://www.khslbc.cz/khs_informace_covid-19/ |
| Moravskoslezský | HTML tabulka | https://koronavirus.msk.cz/ |
| Olomoucký | HTML tabulka | http://www.khsolc.cz/info_verejnost.aspx |
| Pardubický | HTML text ⚠️ | https://www.khspce.cz/aktualni-situace-ve-vyskytu-koronaviru-v-pardubickem-kraji-2/ |
| Plzeňský | Obrázek ⚠️ | http://www.khsplzen.cz/images/KHS/covid19/Plzensky_kraj.jpg |
| Praha | HTML tabulka | http://www.hygpraha.cz/obsah/koronavirus_506_1.html
| Středočeský | ArcGIS API | https://services7.arcgis.com/6U6Ps5FLizN0Qujz/ArcGIS/rest/services/Počet_onemocnění_COVID19_ve_Středočeském_kraji/FeatureServer/0/query |
| Ústecký  | PDF ⚠️| http://www.khsusti.cz/php/kousky/covid19/pocet_testovanych_osob_na_covid19_ustecky_kraj.pdf |
| Zlínský | PDF ⚠️ | http://www.khszlin.cz/ |

Emoji "pozor" ⚠️ označuje zvýšenou potenciální nestabilitu dat a obecně náchylnost ke změnám při aktualizaci ze strany hygienických stanic. To znamená, například, pokud se někdo přepíše, či změní pořadí dat, může (ale nemusí) to rozhodit jednotlivý parser.



