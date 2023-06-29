from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser = webdriver.Chrome()

browser.get('http://quotes.toscrape.com/')
time.sleep(1)
tagia = browser.find_elements(By.XPATH, '//small')
## Lấy tên tác giả
# for i in tagia:
#     print(i.text)
## Lấy link tác giả 
link_tg = browser.find_elements(By.XPATH, "//div[@class='quote']//a[@href]")
for path in link_tg:
    print(path)