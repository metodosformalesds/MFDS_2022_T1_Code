from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

path = 'C:/Users/chay9/OneDrive/Desktop/chromedriver.exe'
options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(path)
driver.get('https://ciudadjuarez.locanto.com.mx/Autos/902/')

entradas = driver.find_elements(By.XPATH, "//div[@class='entries']")

for ent in entradas:
    servicios = driver.find_element(By.XPATH,"//h3[@class='bp_ad__title']")
    print('\n\n')
    print(servicios.text)


#Se selecciono otra pagina por complicaciones, esta ya esta tomando los diferentes titulos de los servicios
