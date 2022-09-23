
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

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  


facebook_link_miami = "https://www.facebook.com/marketplace/miami/search/?query=iphone&exact=false"
listaJson = []

logError = []



def buscarDadosOlx(pages = 2, regiao = "GR"):
  
  
  example = 0 
  
  for x in range(0, pages):
    sleep(2)
    url = "https://www.olx.com.br/celulares/iphone"
    
    if x == 0:
      print("somente uma pagina")
    else:
      url = url + "?o="+str(x)

    PARAMS = {
        "authority":"olx.com.br",
        "method":'GET',
        "path":"celulares/iphone",
        "scheme":"https",
        "referer":"https://www.olx.com.br/celulares/iphone",
        "sec-fetch-mode":"navigate",
        "sec-fetch-size":"same-origin",
        "sec-fetch-user":"?1",
        "upgrade-insecure-request":"1",
        "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10103) AppleWebKit/537.36 (KHTML like Gecko) Chrome/41.0.2272.118 Safari/537.36"
    }    
    page = requests.get(url=url,headers= PARAMS)
    soup = BeautifulSoup(page.content, "lxml")
    items = soup.find_all("a", {"class":["sc-12rk7z2-1 huFwya sc-htoDjs fpYhGm"]})
    
    
    for item in items:
      try:
        url = (item["href"])
        nome = item.find_all("h2",class_=["kgl1mq-0 eFXRHn sc-ifAKCX FMjsQ","kgl1mq-0 eFXRHn sc-ifAKCX gzAEjc"])[0].contents[0]
        valor = item.findAll("span",class_=["m7nrfa-0 eJCbzj sc-fzsDOv kHeyHD","m7nrfa-0 eJCbzj sc-ifAKCX ANnoQ"])[0].contents[0]
        valor = valor.split("R$")[1]
        valor = float(valor.replace(".",""))
        json = {"nome":nome, "valor":valor, "link":url  }
        listaJson.append(json)
        
      except:
        print("procurando error")
       
        
     
    
def buscarDadosMercadoLivre(pages = 2, regiao = "GR"):
  
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
      


def buscarDadosFacebookMiami(manyTimeScroll = 2):
  url = facebook_link_miami
  
  options = Options()
  options.add_argument("start-maximized")
  

  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
  
  driver.get(url)
  
  for a in range(0,manyTimeScroll):
    sleep(2)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight+'+str(100*a)+');')
    sleep(2)
  
  result = driver.page_source
  
  soup = BeautifulSoup(result, "lxml")

  items = soup.find_all("a", attrs={"class":"qi72231t nu7423ey n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l fsf7x5fv rse6dlih s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m cr00lzj9 rn8ck1ys s3jn8y49 icdlwmnq jxuftiz4 l3ldwz01"})
  
  req_dolar = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")

  requisicao_dic = req_dolar.json()

  cotacao_dolar = requisicao_dic["USDBRL"]["bid"]

  cotacao_dolar = round(float(cotacao_dolar))
  
  for item in items:
    try:
      valorTelefone = item.find_all("span", class_="gvxzyvdx aeinzg81 t7p7dqev gh25dzvf tb6i94ri gupuyl1y i2onq4tn b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas f5mw3jnl hxfwr5lz hpj0pwwo sggt6rq5 innypi6y pbevjfx6")[0].contents[0]
      
      valorTelefone = valorTelefone.split()
      valorTelefone = float(valorTelefone[1].replace(".",""))
      nomeTelefone = item.find_all("span",class_="b6ax4al1 lq84ybu9 hf30pyar om3e55n1")[0].contents[0]
      
      
      urlTelefone = "https://www.facebook.com"+item["href"]
      
      json = {"nome":nomeTelefone, "valor":valorTelefone*cotacao_dolar, "link":urlTelefone  }
      
      listaJson.append(json)
      
    except:
      print("erro")
  
  
buscarDadosOlx(pages = 1)
  
filterText = "iPhone 5|iPhone 6|iPhone 7|iPhone SE|iPhone 4|Vitrine|Iphone 7|case|Case|Apple Watch|apple watch|iphone 7|IPHONE 7"  
filterColumnName = "nome"
filterPrice = 1000

timeMinutes = 1800

timerCreateDocument = 30
from datetime import datetime

df = pd.DataFrame(listaJson)

df = df[df[filterColumnName].str.contains(filterText) == False]

df.drop(df[df['valor'] < filterPrice].index, inplace = True)

now = datetime.now()

date_time = now.strftime("%H:%M:%S").replace(",", "")
nameFile = date_time+".xlsx"

print(nameFile)

df.to_excel(""+str(nameFile))


#while True:
#    print("eu")
#    sleep(timerCreateDocument)
