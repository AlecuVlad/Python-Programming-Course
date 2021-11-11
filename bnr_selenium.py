from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.bnr.ro/files/xml/nbrfxrates2021.htm")
table = browser.find_element(By.XPATH, '//*[@id="Data_table"]')
table_text = table.text
data_list = table_text.split('\n')

header = browser.find_element(By.XPATH, '//*[@id="Data_table"]/table/thead/tr').text.split('\n')
dictionary = {i: [] for i in header}

# print(header.text.split('\n'))
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(data_list), len(header)):
        dictionary[header[int(j)]].append(data_list[i])

print(dictionary)

df = pd.DataFrame(dictionary)
df.to_csv("BNR_ALL_DATA.xls")

time.sleep(10)
browser.close()
