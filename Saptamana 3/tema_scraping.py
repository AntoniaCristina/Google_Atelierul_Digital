# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
#
# r = requests.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
# link =  BeautifulSoup(r.text, "html.parser")
#
#
# title = link.find_all('div', attrs={'class': 'entry-content'})
# header = []
# dataset = []
# for i in title:
#     for tr_index in i.find_all('table'):
#         for td_index in tr_index.find_all('tr'):
#             td_list = []
#             if td_index.find_all('td'):#ea a pus th, asa apare pe site
#                 header = [td_index.get_text() for td_index in td_index.find_all('td')]
#             for index, td_value in enumerate(td_index.find_all('td')):
#                 print(index, td_value)
#                 if index == 0 and index == 1:
#                     td_list.append(td_value.get_text())
#                 else:
#                     td_list.append(td_value.get_text().replace(',', '.'))
#             dataset.append(td_list)
# print(dataset)
#
# df = pd.DataFrame(dataset, columns=header)
# df.to_csv("InformareCovid.csv", header=header)

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
ziua_numarul = [20, 21, 22, 23, 24, 25, 26]
for k in ziua_numarul:
    browser.get(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{k}-ianuarie-ora-13-00/")
    table = browser.find_element(by=By.XPATH, value='//*[@id="post-25121"]/div/div/table[1]/tbody')
    rows = table.find_elements(by=By.TAG_NAME, value="tr")
    dictionary = {}
    for i, row in enumerate(rows):
        cells = row.find_elements(by=By.TAG_NAME, value="td")
        for j, cell in enumerate(cells):
            if i == 0:
                dictionary[j] = [cell.text]
            else:
                dictionary[j].append(cell.text)
dictionary[4].append('')
print(dictionary)
df = pd.DataFrame(dictionary)
df.to_csv('InformareCovid.xls')
