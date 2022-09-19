
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



listaJson = []

def buscarDadosOlx(pages = 2, regiao = "GR"):
  
  regiaoBuscar = {"GR":"grande-recife", "CTBA":"grande-recife", "PE":"recife"}
  prefix = {"GR":"pe", "CTBA":"pe", "PE":"pe"}
  
  for x in range(0, pages):
    sleep(2)
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
      


def buscarDadosFacebook(manyTimeScroll = 2):
  url = "https://www.facebook.com/marketplace/106019586096075/search/?query=Iphone&exact=false"
  
  options = Options()
  options.add_argument("start-maximized")
  

  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
  
  driver.get(url)
  
  for a in range(0,manyTimeScroll):
    sleep(4)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight+'+str(100*a)+');')
    sleep(4)
  
  result = driver.page_source
  
  soup = BeautifulSoup(result, "lxml")

  items = soup.find_all("a", attrs={"class":"qi72231t nu7423ey n3hqoq4p r86q59rh b3qcqh3k fq87ekyn bdao358l fsf7x5fv rse6dlih s5oniofx m8h3af8h l7ghb35v kjdc1dyq kmwttqpk srn514ro oxkhqvkx rl78xhln nch0832m cr00lzj9 rn8ck1ys s3jn8y49 icdlwmnq jxuftiz4 l3ldwz01"})
  
  for item in items:
    try:
      valorTelefone = item.find_all("span", class_="gvxzyvdx aeinzg81 t7p7dqev gh25dzvf tb6i94ri gupuyl1y i2onq4tn b6ax4al1 gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas f5mw3jnl hxfwr5lz hpj0pwwo sggt6rq5 innypi6y pbevjfx6")[0].contents[0]
      
      nomeTelefone = item.find_all("span",class_="b6ax4al1 lq84ybu9 hf30pyar om3e55n1")[0].contents[0]
      
      urlTelefone = "https://www.facebook.com"+item["href"]
      
      json = {"nome":nomeTelefone, "valor":valorTelefone, "link":urlTelefone  }
      
      listaJson.append(json)
      
    except:
      print("erro")
  
  
buscarDadosFacebook(10)
buscarDadosMercadoLivre(10)
buscarDadosOlx(10)

df = pd.DataFrame(listaJson)
df.to_json("telefone.json")
