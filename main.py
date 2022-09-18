
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
        
        listaJson.append(json)
        
      except:
        print("erro")
        
     
    
    
#https://lista.mercadolivre.com.br/celulares-telefones/celulares-smartphones/iphone/usado/iphone_NoIndex_True#applied_filter_id%3DBRAND%26applied_filter_name%3DMarca%26applied_filter_order%3D3%26applied_value_id%3D9344%26applied_value_name%3DApple%26applied_value_order%3D5%26applied_value_results%3D7886%26is_custom%3Dfalse
def buscarDadosMercadoLivre(pages = 2, regiao = "GR"):
  
  for x in range(0, pages):
    sleep(2)
    print("Loop" + (str(x)))
    url = "https://lista.mercadolivre.com.br/celulares-telefones/celulares-smartphones/iphone/usado/"
    
    if x == 0:
      print("somente uma pagina")
    else:
      url = url + "_Desde_"+str(x*50+1)+"_NoIndex_True"
      print(url)
      
    path = "/celulares-telefones/celulares-smartphones/iphone/usado/"
    
    PARAMS = {
        "authority":"lista.mercadolivre.com.br",
        "method":'GET',
        "path":path,
        "scheme":"https",
        "referer":url,
        "sec-fetch-mode":"navigate",
        "sec-fetch-size":"same-origin",
        "sec-fetch-user":"?1",
        "upgrade-insecure-request":"1",
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10103) AppleWebKit/537.36 (KHTML like Gecko) Chrome/41.0.2272.118 Safari/537.36"
    }
    
    page = requests.get(url=url,headers=PARAMS)
    
    soup = BeautifulSoup(page.content, "lxml")
    
    items = soup.find_all("li", {"class":"ui-search-layout__item"})
    
    for item in items:
      try:
        nomeTelefone = item.findAll("h2")[0].contents[0]
        valorTelefone = item.findAll("span",class_="price-tag-fraction")[0].contents[0]
        valorTelefone = float(valorTelefone.replace(".",""))
        urlTelefone = item.find("a")["href"]
        
        json = {"nome":nomeTelefone, "valor":valorTelefone, "link":urlTelefone  }
        listaJson.append(json)
       
      except:
        print("erro")
        
    
    
buscarDadosMercadoLivre(pages = 1)

df = pd.DataFrame(listaJson)
#df.to_excel("telefone.xlsx")
df.to_html("index.html")
