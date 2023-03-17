import requests
from csv import writer
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import itertools


#selenium Path
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.nike.com/w/mens-shoes-nik1zy7ok')

#PAGE SCROLLING
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
SCROLL_PAUSE_TIME = .5
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
Wname=driver.find_elements(By.CLASS_NAME, "product-card__title")
Wprice=driver.find_elements(By.CLASS_NAME, "product-card__price")
Wcolor=driver.find_elements(By.CLASS_NAME, "product-card__product-count")

#Make 3 seperate list to translate over to text
name=[]
price=[]
color=[]
for i in Wname :
  name.append(i.text)
for i in Wprice:
  price.append(i.text)
for i in Wcolor:
  color.append(i.text)

#making CSV 
new_list=[]
with open('Menshoes.csv','w', encoding='utf8',newline='') as f:
  thewriter= writer(f)
  header=['Name','Price','#Color']
  thewriter.writerow(header)
  for n,p,q in itertools.zip_longest(name,price,color):
    if n:
        new_list.append(n)
    if p:
        new_list.append(p)
    if q:
        new_list.append(q)
    info = [n,p,q]
    thewriter.writerow(info)


