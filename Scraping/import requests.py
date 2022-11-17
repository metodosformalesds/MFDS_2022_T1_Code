from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

path = 'C:/Users/chay9/OneDrive/Desktop/chromedriver.exe'
options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(path)
driver.get('https://ciudadjuarez.locanto.com.mx/Autos/902/')

servicios = driver.find_elements(By.XPATH,"//h3[@class='bp_ad__title']")
servicios = [ serv.text for serv in servicios ]
print(servicios)

#price //div[@class='bp_ad__price']
#Information //a[@class='bp_ad__desc_link']

