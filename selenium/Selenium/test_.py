from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service=Service(ChromeDriverManager().install())
browser = webdriver.Chrome()

browser.get('')

sleep(2)