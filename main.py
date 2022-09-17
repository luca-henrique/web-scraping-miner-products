
import pandas as pd
import numpy as np

from bs4 import BeautifulSoup

import json

from difflib import SequenceMatcher
from selenium import webdriver
import time
from datetime import date

import re

import requests

#https://pe.olx.com.br/grande-recife/celulares

def buscarDadosOlx(pages = 2, regiao = "GR"):
  
  regiaoBuscar = {"GR":"grande-recife", "CTBA":"grande-recife", "PE":"recife"}
  prefix = {"GR":"pe", "CTBA":"pe", "PE":"pe"}
  
  for x in range(0, pages):
    print("Loop" + (str(x)))
    url = "https://"+prefix[regiao]+".olx.com.br/"+regiaoBuscar[regiao]+"/celulares/iphone"
    
    if x == 0:
      print("somente uma pagina")
    else:
      url = url + "?o="+str(x)

    PARAMS = {
        "authority":"pe.olx.com.br",
        "method":'GET',
        "path":"/grande-recife/celulares/iphone",
        "scheme":"https",
        "referer":"https://pe.olx.com.br/grande-recife/celulares/iphone",
        "sec-fetch-mode":"navigate",
        "sec-fetch-size":"same-origin",
        "sec-fetch-user":"?1",
        "upgrade-insecure-request":"1",
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10103) AppleWebKit/537.36 (KHTML like Gecko) Chrome/41.0.2272.118 Safari/537.36"
    }    
    page = requests.get(url=url,headers= PARAMS)
    soup = BeautifulSoup(page.content, "lxml")
    items = soup.find_all("li", {"class":["sc-1fcmfeb-2 fvbmlV","sc-1fcmfeb-2 kZiBLm","sc-1fcmfeb-2 fvbmlV"]})
    
    
    print(len(items))
    
    for item in items:
      try:
        print(item.findAll("h2")[0].contents[0])
      except:
        print("erro")
    
buscarDadosOlx()
