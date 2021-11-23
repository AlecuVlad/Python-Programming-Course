import re
import time
import unidecode
import datetime as dt
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_month(number: int) -> str:
    match number:
        case 1:
            return 'ianuarie'
        case 2:
            return 'februarie'
        case 3:
            return 'martie'
        case 4:
            return 'aprilie'
        case 5:
            return 'mai'
        case 6:
            return 'iunie'
        case 7:
            return 'iulie'
        case 8:
            return 'august'
        case 9:
            return 'septembrie'
        case 10:
            return 'octombrie'
        case 11:
            return 'noiembrie'
        case 12:
            return 'decembrie'


dictionary = {}
header_items = []
header_len = 0

day = input("Alege ziua: ")
month = input("Alege luna: ")
req_date = dt.datetime(2021, int(month), int(day))

for date in range(0, 7):
    # get the date
    old_date = req_date - dt.timedelta(days=date)
    old_date_str = old_date.strftime("%m:%d:%y")

    list_date = old_date_str.split(':')
    curr_day = str(int(list_date[1]))
    month_str = get_month(int(list_date[0]))

    # create URL
    prefix_url = "https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-"
    mid_url = curr_day + '-' + month_str
    suffix_url = "-ora-13-00/"

    # get table
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(prefix_url + mid_url + suffix_url)
    table_rows = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/main/article/div/div/table[1]')\
        .text.split('\n')

    # create header
    if len(header_items) == 0:
        header = table_rows.pop(0)  # remove and get header
        header_items = re.findall('[A-Z][^A-Z]*', header)
        header_len = len(header_items)
    else:
        table_rows.pop(0)

    # create dictionary
    if dictionary == {}:
        dictionary = {i: [] for i in range(5)}

    # add date
    dictionary[0].append(old_date_str.replace(':', '.'))
    for column in range(1, header_len):
        dictionary[column].append('')

    # modify special number in table
    table_rows[-2] = table_rows[-2].replace('*', '')

    # remove last character if it is ' '
    for i in range(1, 3):
        table_rows[-i] = table_rows[-i].strip()
        table_rows[-i] = table_rows[-i] + ' '

    table_rows[-1] = ' ' + table_rows[-1]

    # get all elements of the table
    all_elems = [i for row in table_rows
                 for elem in reversed(row[::-1].split(' ', maxsplit=3))
                 for i in elem[::-1].split(' ', maxsplit=1)]

    all_elems = header_items + all_elems

    # replace ',' with '.' for 'Incidenta'
    for i in range(4, len(all_elems), header_len):
        all_elems[i] = all_elems[i].replace(',', '.')

    # replace '.' with ',' for the TOTAL
    for i in range(-3, -1):
        all_elems[i] = all_elems[i].replace('.', ',')

    # add data in dictionary
    for column in range(header_len):
        for idx in range(0 + column, len(all_elems), header_len):
            dictionary[column].append(unidecode.unidecode(all_elems[idx]))

    # add space between days
    for column in range(header_len):
        dictionary[column].append('')

    time.sleep(2)
    browser.close()

# add dictionary in xls
df = pd.DataFrame.from_dict(dictionary, orient='index')
df = df.transpose()
df.to_csv("Covid_Data.xls")
