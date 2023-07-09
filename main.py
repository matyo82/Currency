import requests, csv
from bs4 import BeautifulSoup
from DataBase import addTodatabase, updatePrice
# Send a GET request to the website
url = "https://www.tgju.org/currency"
response = requests.get(url)

# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the currency rates
tables = soup.find_all('table',{"class": "data-table"})

f = open('arz.csv','a+')
writer = csv.writer(f)
for table in tables:
    rows = table.find_all('tr')

    # Iterate over the rows and extract the currency data
    for row in rows[1:]:  # Skip the header row
        cells = row.find_all('td')
        thCell = row.find_all('th')
        spanCell = thCell[0].text.strip()
        currency = cells[0].text.strip()
        price = cells[2].text.strip()
        print(f"Currency: {spanCell}\tPrice: {price}")
        price = int(price.replace(",",""))
        data = [spanCell,price]
        # for add a item in data base
        # addTodatabase(spanCell, price)
        # for update price data base
        updatePrice(price,spanCell)
        writer.writerow(data)
f.close