

import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import json

from difflib import SequenceMatcher
from time import sleep
from datetime import date


import requests


listaJson = []

logError = []


def buscarDadosMercadoLivre(pages=2, regiao="GR"):

    for x in range(0, pages):
        sleep(2)

        url = "https://lista.mercadolivre.com.br/celulares-telefones/celulares-smartphones/iphone/usado/"

        if x == 0:
            print("somente uma pagina")
        else:
            url = url + "_Desde_"+str(x*50+1)+"_NoIndex_True"
            print(url)

        path = "/celulares-telefones/celulares-smartphones/iphone/usado/"

        PARAMS = {
            "authority": "lista.mercadolivre.com.br",
            "method": 'GET',
            "path": path,
            "scheme": "https",
            "referer": url,
            "sec-fetch-mode": "navigate",
            "sec-fetch-size": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-request": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10103) AppleWebKit/537.36 (KHTML like Gecko) Chrome/41.0.2272.118 Safari/537.36"
        }

        page = requests.get(url=url, headers=PARAMS)

        soup = BeautifulSoup(page.content, "lxml")

        items = soup.find_all("li", {"class": "ui-search-layout__item"})

        for item in items:
            try:
                nomeTelefone = item.findAll("h2")[0].contents[0]
                valorTelefone = item.findAll(
                    "span", class_="price-tag-fraction")[0].contents[0]
                valorTelefone = float(valorTelefone.replace(".", ""))
                urlTelefone = item.find("a")["href"]

                json = {"nome": nomeTelefone,
                        "valor": valorTelefone, "link": urlTelefone}
                listaJson.append(json)

            except:
                print("erro")
