from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

path = 'C:/Users/chay9/OneDrive/Desktop/chromedriver.exe'
options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(path)
driver.get('https://ciudadjuarez.locanto.com.mx/Autos/902/')

servicios_title = driver.find_elements(By.XPATH,"//h3[@class='bp_ad__title']")
servicios_title = [ serv.text for serv in servicios_title ]

servicios_price = driver.find_elements(By.XPATH, "//div[@class='bp_ad__price']")
servicios_price = [ pri.text for pri in servicios_price ]

servicios_info = driver.find_elements(By.XPATH, "//a[@class='bp_ad__desc_link']")
servicios_info = [ inf.text for inf in servicios_info ]

Publicaciones = {
    "Titulo": servicios_title,
    "Precio": servicios_price,
    "Informacion": servicios_info
}

df = pd.DataFrame(Publicaciones) 
df.to_csv("Publicaciones.csv")
#price //div[@class='bp_ad__price']
#Information//a[@class='bp_ad__desc_link']

