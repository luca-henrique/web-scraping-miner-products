
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
        
      }
    
buscarDadosOlx()
