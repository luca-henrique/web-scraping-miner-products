
from bs4 import BeautifulSoup
from time import sleep
import requests


def buscarDadosOlx(pages=2):

    for x in range(0, pages):
        sleep(2)
        url = "https://www.olx.com.br/celulares/iphone"

        if x == 0:
            print("somente uma pagina")
        else:
            url = url + "?o="+str(x)

        PARAMS = {
            "authority": "olx.com.br",
            "method": 'GET',
            "path": "celulares/iphone",
            "scheme": "https",
            "referer": "https://www.olx.com.br/celulares/iphone",
            "sec-fetch-mode": "navigate",
            "sec-fetch-size": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-request": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10103) AppleWebKit/537.36 (KHTML like Gecko) Chrome/41.0.2272.118 Safari/537.36"
        }

        page = requests.get(url=url, headers=PARAMS)
        soup = BeautifulSoup(page.content, "lxml")
        items = soup.find_all(
            "a", {"class": ["sc-12rk7z2-1 huFwya sc-htoDjs fpYhGm"]})

        return itemsInList(items)


def itemsInList(items=[]):
    data = []
    for item in items:
        try:
            url = (item["href"])
            nome = item.find_all("h2", class_=[
                                 "kgl1mq-0 eFXRHn sc-ifAKCX FMjsQ", "kgl1mq-0 eFXRHn sc-ifAKCX gzAEjc"])[0].contents[0]
            valor = item.findAll("span", class_=[
                                 "m7nrfa-0 eJCbzj sc-fzsDOv kHeyHD", "m7nrfa-0 eJCbzj sc-ifAKCX ANnoQ"])[0].contents[0]
            valor = valor.split("R$")[1]
            valor = float(valor.replace(".", ""))
            json = {"nome": nome, "valor": valor, "link": url}
            data.append(json)

        except:
            print("procurando error")

    return data
