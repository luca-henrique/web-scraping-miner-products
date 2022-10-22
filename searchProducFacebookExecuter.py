
import pandas as pd
from time import sleep
from datetime import datetime

from filterFileFunctions import filterByList, filterByPrice
from searchProductFacebook import searchProductFacebook

timeWaitingNextSearch = 1200
countPageSearch = 1

listaJson = searchProductFacebook()
      
df = pd.DataFrame(listaJson)

df = filterByList(df)
df = filterByPrice(df)

now = datetime.now()

date_time = now.strftime(
         "%H:%M %d/%m/%Y").replace(",", "").replace(" ", "-").replace("/", "-")
nameFile = date_time+".xlsx"
df.to_excel(uf+str(nameFile))
