"""_summary_

    Probando la instalacion de selenium

"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = False
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),options=options)
driver.maximize_window()

driver.get('https://alirafael.com/')
sleep(2)

driver.close()
