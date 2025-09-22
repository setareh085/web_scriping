import requests
from bs4 import BeautifulSoup
import mysql.connector
from sklearn.tree import DecisionTreeRegressor
import numpy as np

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="countries"
)

# Scrape data from the website
headers = {"User-Agent": "Mozilla/5.0"}
try:
    response = requests.get("https://www.scrapethissite.com/pages/simple/", headers=headers, timeout=30)
    response.raise_for_status()
except requests.RequestException as e:
    print("Error connecting to the website:", e)
    exit()

soup = BeautifulSoup(response.text, "html.parser")
countries = soup.find_all("div", class_="country")

# Use a single cursor for all INSERT operations
with mydb.cursor() as cursor:
    for c in countries:
        country_name = c.find("h3", class_="country-name").text.strip()
        country_capital = c.find("span", class_="country-capital").text
        population = c.find("span", class_="country-population").text
        area = c.find("span", class_="country-area").text

        # Extract capital value
        capital_value = country_capital.split(":")[1].strip() if ":" in country_capital else country_capital.strip()
        population_value = int(population.replace(",", "").strip())
        area_value = float(area.replace(",", "").strip())

        # Prevent duplicate entries
        sql = """
        INSERT INTO country (country_name, capital, population, area)
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE capital=VALUES(capital), population=VALUES(population), area=VALUES(area)
        """
        val = (country_name, capital_value, population_value, area_value)
        cursor.execute(sql, val)

    # Commit all changes
    mydb.commit()

# Read data from the database for the model
x, y = [], []
with mydb.cursor() as cursor:
    cursor.execute("SELECT population, area FROM country")
    for pop, area in cursor.fetchall():
        x.append(pop)
        y.append(area)

mydb.close()

# Prepare data for Scikit-Learn
x = np.array(x).reshape(-1, 1)  # X must be 2D
y = np.array(y)                  # y can be 1D

# Create and train the Decision Tree Regressor
clf = DecisionTreeRegressor()
clf.fit(x, y)

# Predict area based on new population input
new_population = int(input("population: "))
answer = clf.predict([[new_population]])  # Input must be 2D
print(f"Projected area {answer[0]} km²")
