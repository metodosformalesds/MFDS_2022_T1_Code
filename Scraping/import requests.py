from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


URL ='https://dallas.craigslist.org/search/sss?query=cars#search=1~gallery~0~0'
s = Service('/Users/chay9/OneDrive/Desktop/chromedriver')

driver = webdriver.Chrome(service=s)
driver.get(URL)
print()
matches = driver.find_elements(By.CLASS_NAME, "gallery-card")

print(matches)