import requests
from csv import writer
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import itertools


#selenium Path
url= 'https://www.champssports.com/category/mens/shoes.html?currentPage=0'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),)
driver.maximize_window()
driver.get(url)
clickobj2= driver.find_element(By.ID,'touAgreeBtn')
time.sleep(3)
clickobj2.click()


#PAGE SCROLLING
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
SCROLL_PAUSE_TIME = .5
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, 200);")
    clickobj= driver.find_element(By.LINK_TEXT,'Next')
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
#Grab element
clickobj= driver.find_element(By.LINK_TEXT,'Next')
Wname = driver.find_elements(By.CLASS_NAME,'ProductName-primary')
Wprice = driver.find_elements(By.CLASS_NAME,'ProductPrice')



name = []
price = []
condition = True


while condition:
  #PAGE SCROLLING
  # Get scroll height
  last_height = driver.execute_script("return document.body.scrollHeight")
  SCROLL_PAUSE_TIME = .5
  while True:
      # Scroll down to bottom
      driver.execute_script("window.scrollTo(0, 140);")
      
      # Wait to load page
      time.sleep(SCROLL_PAUSE_TIME)
      # Calculate new scroll height and compare with last scroll height
      new_height = driver.execute_script("return document.body.scrollHeight")
      if new_height >= last_height:
          break
      last_height = new_height
  clickobj= driver.find_element(By.LINK_TEXT,'Next')
  Wname = driver.find_elements(By.CLASS_NAME,'ProductName-primary')
  Wprice =driver.find_elements(By.CLASS_NAME,'ProductPrice')
  for i in Wname:
    name.append(i.text)
  for i in Wprice:
    price.append(i.text)
  new_list =[]
  with open('Menshoes.csv','a', encoding='utf8',newline='') as f:
    thewriter= writer(f)
    header=['Name','Price','#Color']
    thewriter.writerow(header)
    for n,p in itertools.zip_longest(name,price):
      if n:
          new_list.append(n)
      if p:
          new_list.append(p)
      info = [n,p]
      thewriter.writerow(info)
      print(info)
  clickobj.click()
