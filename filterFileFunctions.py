
from constants import minPricePhone, maxPricePhone, filterPhoneList


def filterByList(file_xlsx):
    loadFiler = file_xlsx[file_xlsx.nome.isin(filterPhoneList) == False]
    return loadFiler


def filterByPrice(file_xlsx):
    loadFiler = file_xlsx.loc[(file_xlsx.valor >= minPricePhone) & (
        file_xlsx.valor <= maxPricePhone)]
    return loadFiler
