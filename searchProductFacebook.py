
import pandas as pd
import numpy as np

from bs4 import BeautifulSoup

import json

from difflib import SequenceMatcher
from selenium import webdriver
from time import sleep
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def searchProductFacebook(manyTimeScroll=10, listaJson=[]):
    url = "https://www.facebook.com/marketplace/104941129541687/search/?query=ssd"

    options = Options()
    options.add_argument("start-maximized")

    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    driver.get(url)

    for a in range(0, manyTimeScroll):
        sleep(2)
        driver.execute_script(
            'window.scrollTo(0, document.body.scrollHeight+'+str(100*a)+');')
        sleep(2)

    result = driver.page_source

    soup = BeautifulSoup(result, "lxml")

    items = soup.find_all("a", attrs={
                          "class": "qi72231t nu7423ey n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l fsf7x5fv rse6dlih s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m cr00lzj9 rn8ck1ys s3jn8y49 icdlwmnq jxuftiz4 l3ldwz01"})


    print(items)

    for item in items:
        try:
            priceItem = item.find_all(
                "span", class_="gvxzyvdx aeinzg81 t7p7dqev gh25dzvf tb6i94ri gupuyl1y i2onq4tn b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas f5mw3jnl hxfwr5lz hpj0pwwo sggt6rq5 innypi6y pbevjfx6")[0].contents[0]

            priceItem = priceItem.split()
            priceItem = float(priceItem[1].replace(".", ""))
            nameItem = item.find_all(
                "span", class_="b6ax4al1 lq84ybu9 hf30pyar om3e55n1")[0].contents[0]

            url = "https://www.facebook.com"+item["href"]

            json = {"name": nameItem, "valor": priceItem, "link": url}

            listaJson.append(json)

            return listaJson

        except:
            print("erro")
