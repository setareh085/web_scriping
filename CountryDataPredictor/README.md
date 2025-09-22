# ✅ Country Scraper

A simple Python script that scrapes country information (name, capital, population, area) from [Scrape This Site](https://www.scrapethissite.com/pages/simple/) and saves it into a MySQL database.

---

## 📂 Project Structure

Country-Scraper/

├── scrape_countries.py # Main script

├── README.md # Documentation


---

## ⚙️ Requirements

- Python 3.10+
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `mysql-connector-python`

- MySQL Database:
  - Database: `world`
  - Table: `countries`

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/USERNAME/Country-Scraper.git
```
Navigate into the project folder:
```bash
cd Country-Scraper
```
Install dependencies:
```bash
pip install -r requirements.txt
```
## 🛠️ Database Setup
```bash

CREATE DATABASE world;
USE world;

CREATE TABLE countries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_name VARCHAR(100),
    capital VARCHAR(100),
    population BIGINT,
    area FLOAT
);
```
## 📝 Features

* ➕ Scrapes the first 20 countries

* 💾 Inserts data into MySQL database

* 📊 Stores country name, capital, population, and area

* 🧹 Cleans and formats scraped text

## 📌 Usage

Run the script:
```bash
python scrape_countries.py
```
## 📄 License

This project is licensed under the [MIT License](LICENSE).


## 👩‍💻 Author

Setareh

## 📘 What I Learned

* How to scrape data with BeautifulSoup

* How to clean and format scraped data

* How to connect Python with MySQL

* How to insert data programmatically into a database
