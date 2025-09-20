from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import csv
web = r"https://divar.ir/s/tehran"
path = r"C:\webdrives\chromedriver.exe"
driver = webdriver.Chrome(service=Service(path))
driver.get(web)
a = set()

height = driver.execute_script("return document.body.scrollHeight")
scroll = 10
h = 0
while h < scroll:
        
        posts = driver.find_elements(By.XPATH,'//div[contains(@class,"post-card")]')
        for post in posts:
            tag = post.find_elements(By.XPATH,'.//span[@class="kt-post-card__red-text"]')
            if len(tag)>0:
                title = post.find_elements(By.XPATH,'.//h2[@class="kt-post-card__title"]')
                if any("نردبان" in t.text for t in tag):
                    if title:   # اگر عنوان پیدا شد
                        title_text = title[0].text.strip()
                        if title_text and title_text not in a:
                            a.add(title_text)
                    # Write the title to the CSV file
                    
                        else:
                            alt = post.find_elements(By.XPATH, './/div[contains(@class,"kt-post-card__title")]')
                            if alt:
                                title_text = alt[0].text.strip()
                            if title_text and title_text not in a:
                                a.add(title_text)
                              
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        new = driver.execute_script("return document.body.scrollHeight")
        if new == height:
            break
        height = new
        h += 1
        
driver.quit()

with open("posts.csv", "a", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    for title in a:
        writer.writerow([title])
