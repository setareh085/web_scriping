import requests
from bs4 import BeautifulSoup
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="world"
)
response = requests.get("https://www.scrapethissite.com/pages/simple/")
soup = BeautifulSoup(response.text,"html.parser")
country =soup.find_all("div", class_ = "country")
count = 0
for c in country:
    if count != 20:
        count += 1
        country_name = c.find("h3", class_="country-name").text.strip()
        country_capital = c.find("span", class_ = "country-capital").text
        population = c.find("span", class_ = "country-population").text
        area = c.find("span", class_ = "country-area").text
        if ":" in country_capital:
            capital_value = country_capital.split(":")[1].strip()
        else:
            capital_value = country_capital.strip()

        population_value = int(population.replace(",", "").strip())
        area_value = float(area.replace(",", "").strip())

        cursor = mydb.cursor()
        sql = "INSERT INTO countries (country_name, capital, population, area) VALUES (%s, %s, %s, %s)"
        val = (country_name, capital_value, population_value, area_value)
        cursor.execute(sql, val)
        mydb.commit()
        cursor.close()
    else:
        break
    
mydb.close()
