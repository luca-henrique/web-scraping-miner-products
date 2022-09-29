
import pandas as pd
from time import sleep
from datetime import datetime

from filterFileFunctions import filterByList, filterByPrice
from searchProductOlx import buscarDadosOlx

timeWaitingNextSearch = 1200
countPageSearch = 100

while True:
    listaJson = buscarDadosOlx(pages=countPageSearch, UF = "pe")
    
    df = pd.DataFrame(listaJson)

    df = filterByList(df)

    df = filterByPrice(df)

    now = datetime.now()

    date_time = now.strftime(
       "%H:%M %d/%m/%Y").replace(",", "").replace(" ", "-").replace("/", "-")
    nameFile = date_time+".xlsx"

    df.to_excel(""+str(nameFile))

    sleep(timeWaitingNextSearch)
