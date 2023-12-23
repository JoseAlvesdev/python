from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service=Service(ChromeDriverManager().install())
browser = webdriver.Chrome()

browser.get('https://stackoverflow.com/questions/11005457/how-do-i-remove-delete-a-virtualenv')

sleep(2)