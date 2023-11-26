from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.infomoney.com.br/')

sleep(2)

dados = driver.find_element(By.ID, 'menu-side').text

print(dados)