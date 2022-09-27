
import pandas
import glob
from filterFileFunctions import filterByList, filterByPrice

file_xlsx = pandas.DataFrame()
for file in glob.glob("*.xlsx"):
    read_file_xlsx = pandas.read_excel(file)
    file_xlsx = file_xlsx.append(read_file_xlsx)


file_xlsx.drop_duplicates('link', keep='last')

loadFiler = filterByList(file_xlsx)

loadFiler = filterByPrice(loadFiler)

loadFiler.to_excel("arquivo_filtrado.xlsx")
