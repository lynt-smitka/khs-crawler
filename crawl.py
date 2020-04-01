#!/usr/local/bin/python3.7

from libs import kraj_jc
from libs import kraj_vys
from libs import kraj_hk
from libs import kraj_lib
from libs import kraj_olo
from libs import kraj_usti
from libs import kraj_par
from libs import kraj_kv
from libs import kraj_plz
from libs import kraj_strc
from libs import kraj_pha
from libs import kraj_brn
from libs import kraj_zl
from libs import kraj_msk

import pygsheets
import pandas as pd

from datetime import datetime


# Connect to spreadsheet
gc = pygsheets.authorize(service_file='./conf/crawling_auth.json')
sh = gc.open_by_key('1FFEDhS6VMWon_AWkJrf8j3XxjZ4J6UI1B2lO3IW-EEc')
wks = sh.worksheet_by_title('Test crawl')

df = wks.get_as_df(include_tailing_empty=False, include_tailing_empty_rows=False, numerize=False)
df = df.set_index('Okres')

kraje = [
  
  kraj_jc.web().crawl(),
  kraj_vys.web().crawl(),
  kraj_hk.web().crawl(),
  kraj_lib.web().crawl(),
  kraj_olo.web().crawl(),
  kraj_usti.web().crawl(),
  kraj_par.web().crawl(),
  kraj_kv.web().crawl(),
  kraj_plz.web().crawl(),
  kraj_strc.web().crawl(),
  kraj_pha.web().crawl(),
  kraj_brn.web().crawl(),
  kraj_zl.web().crawl(),
  kraj_msk.web().crawl(),
  
  ]

date = datetime.strftime(datetime.now(), '%Y-%m-%d')

for okresy in kraje:
  for okres in okresy:
    df.at[okres['okres'], date] = okres['hodnota']

wks.clear()
wks.set_dataframe(df,(1,1),copy_index=True, nan='-')
wks.update_value('A1','Okres')

