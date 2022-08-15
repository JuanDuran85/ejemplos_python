"""_summary_

    Utilizando Selenium para realizar prueba de login en web

"""

import os
from time import sleep

from dotenv import load_dotenv
from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()

pass_in_user = os.environ.get('PASS_IN_USER')
email_user = os.environ.get('EMAIL_USER')
url_web = os.environ.get('URL_WEB')

options = Options()
options.headless = False
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),options=options)
driver.maximize_window()

driver.get(url_web)

usuario = driver.find_element(by=By.ID, value="user_email")
boton_siguiente = driver.find_element(by=By.CLASS_NAME, value="form__btn")

usuario.send_keys(email_user)
boton_siguiente.click()

password_in = driver.find_element(by=By.ID, value="user_password")
boton_siguiente = driver.find_element(by=By.CLASS_NAME, value="form__btn")
password_in.send_keys(pass_in_user)
boton_siguiente.click()

boton_siguiente = driver.find_element(by=By.ID, value="toggle-aside-my-account")
boton_siguiente.click()

sleep(4)
driver.find_element(by=By.LINK_TEXT, value="Cerrar Sesión").click()





