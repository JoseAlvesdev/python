from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://statusinvest.com.br/')

sleep(2)

dados = driver.find_elements(By.CLASS_NAME, 'text-main')[0].text

print(dados)