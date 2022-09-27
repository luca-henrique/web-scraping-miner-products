import pandas as pd

from filterFileFunctions import filterByList, filterByPrice

file_xlsx = pd.read_excel('11:15-26-09-2022.xlsx', index_col=0)

loadFiler = filterByList(file_xlsx)

loadFiler = filterByPrice(loadFiler)

loadFiler.to_excel("arquivo.xlsx")

print(loadFiler)
