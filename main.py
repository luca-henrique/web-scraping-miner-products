
import pandas as pd
import numpy as np

from bs4 import BeautifulSoup

import json

from difflib import SequenceMatcher
from selenium import webdriver
from time import sleep
from datetime import date

import re

import requests

#https://pe.olx.com.br/grande-recife/celulares

listaJson = []

def buscarDadosOlx(pages = 2, regiao = "GR"):
  
  regiaoBuscar = {"GR":"grande-recife", "CTBA":"grande-recife", "PE":"recife"}
  prefix = {"GR":"pe", "CTBA":"pe", "PE":"pe"}
  
  for x in range(0, pages):
    sleep(2)
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
    
    for item in items:
      try:
        nomeTelefone = item.findAll("h2")[0].contents[0]
        
      
        
        valorTelefone = item.findAll("span",class_="m7nrfa-0 eJCbzj sc-fzsDOv kHeyHD")[0].contents[0]
        valorTelefone = valorTelefone.split("R$")[1]
        valorTelefone = float(valorTelefone.replace(".",""))
        
        informacoesDiaHoraPostagem = item.findAll("span",class_="sc-11h4wdr-0 javKJU sc-fzsDOv dTHJIA")[0].contents[0]
      
        horaPostagem = informacoesDiaHoraPostagem.split()[1]
        diaPostagem =  informacoesDiaHoraPostagem.split()[0].replace(",","")
        
        urlTelefone = item.find("a")["href"]

        enderecoItem = item.find_all("span",class_="sc-1c3ysll-1 iDvjkv sc-fzsDOv dTHJIA")[0].contents[0]
        
        json = {"dia_postagem":diaPostagem, "hora_postagem":horaPostagem, "nome":nomeTelefone, "valor":valorTelefone, "link":urlTelefone, "regiao": enderecoItem  }

        
        if ('IPhone' in nomeTelefone) or ('Iphone' in nomeTelefone):
          print(test)


        listaJson.append(json)
        
      except:
        print("erro")
        
      for telefone in listaJson:
          
        if(telefone['nome'].toLower() == "Iphone X".toLower()):
          print(telefone['nome'])
    
buscarDadosOlx(pages = 1)

df = pd.DataFrame(listaJson)

#df.to_excel("telefone.xlsx")
df.to_html("index.html")
