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
import undetected_chromedriver as uc


#selenium Path
url= 'https://www.finishline.com/store/men/shoes/_/N-1737dkj?mnid=men_shoes'
time.sleep(5)
driver = uc.Chrome(service=Service(ChromeDriverManager().install()),)
time.sleep(5)
driver.maximize_window()
driver.get(url)


name=[]
price=[]
conditions= True

while conditions:
  # Get scroll height
  last_height = driver.execute_script("return document.body.scrollHeight")
  SCROLL_PAUSE_TIME = 1
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
  clickobj = driver.find_element(By.XPATH, '//*[@id="mainColumn"]/div[4]/div[5]/button[2]')
  Wname = driver.find_elements(By.CLASS_NAME,'product-name')
  Wprice = driver.find_elements(By.CLASS_NAME,'fullPrice')
  for i in Wname :
    name.append(i.text)
  for i in Wprice:
    price.append(i.text)
    
  new_list=[]
  with open('Menshoes.csv','w', encoding='utf8',newline='') as f:
    thewriter= writer(f)
    header=['Name','Price']
    thewriter.writerow(header)
    for n,p in itertools.zip_longest(name,price):
      if n:
          new_list.append(n)
      if p:
          new_list.append(p)
      info = [n,p]
      thewriter.writerow(info)
      print(info)
    try:
      clickobj.click()  
    except:
      conditions=False