from selenium import webdriver
from selenium.webdriver.common.by import By

path = 'C:/Users/chay9/OneDrive/Desktop/chromedriver.exe'
options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome(path)
driver.get('https://ciudadjuarez.locanto.com.mx/Servicios/S/')

servicios = driver.find_elements(By.XPATH,"//h3[@class='bp_ad__title']")
print(servicios)

#Se selecciono otra pagina por complicaciones, esta ya esta tomando los diferentes titulos de las paginas
