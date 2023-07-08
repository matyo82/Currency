import requests
from bs4 import BeautifulSoup
import csv
# Making a GET request
r = requests.get('https://www.tgju.org/profile/price_dollar_rl')
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find('div', class_='stocks-header-content')
titel_fa = s.find('h1', class_='title') #               titel for parsian
titel_fa = titel_fa.text.strip()
titel_en = s.find('div', class_='line header-tag') #    titel for en
titel_en = titel_en.text.strip()
price = s.find('span', class_='price') #                find price
price = price.text.strip()
price = int(price.replace(",",""))
valu = 'ریال'
print(f'price {titel_en}: {price} - valu: {valu} \ntitel en: {titel_en} - titel-fa: {titel_fa}')

file_name = 'arz.csv'
try:
    open(file_name)
except:
    print("not fine file!!")

file = open(file_name,"+a")
data = [titel_fa, titel_en, price, valu]
writer = csv.writer(file)
writer.writerow(data)
file.close()