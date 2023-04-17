from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



def pay(phone_n, price):
    options = Options()
    options.add_argument("user-data-dir=/home/sergey/SeleniumProfile")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.tinkoff.ru/collectmoney/action/create/?tab=invoiceCreate')
    time.sleep(2)
    try:
        element = driver.find_element(By.ID, "pinCodeField")
        if element:
            pin1 = driver.find_element(By.ID, 'pinCode0')
            pin2 = driver.find_element(By.ID, 'pinCode1')
            pin3 = driver.find_element(By.ID, 'pinCode2')
            pin4 = driver.find_element(By.ID, 'pinCode3')
            #и пин код не солью тоже
            pin1.send_keys('X')
            pin2.send_keys('X')
            pin3.send_keys('X')
            pin4.send_keys('X')

    except NoSuchElementException:

        time.sleep(2)
        phone = driver.find_element(By.NAME, 'phone')

        phone.send_keys(phone_n)

        phone.send_keys(Keys.ARROW_DOWN)
        phone.send_keys(Keys.ARROW_DOWN)
        phone.send_keys(Keys.RETURN)

        amount = driver.find_element(By.NAME, 'moneyAmount')
        amount.send_keys(price)

        create = driver.find_element(By.CLASS_NAME, 'Button-module__content_kpdCF')
        create.click()

        time.sleep(4)
    else:
        time.sleep(2)
        phone = driver.find_element(By.NAME, 'phone')

        phone.send_keys(phone_n)

        phone.send_keys(Keys.ARROW_DOWN)
        phone.send_keys(Keys.ARROW_DOWN)
        phone.send_keys(Keys.RETURN)

        amount = driver.find_element(By.NAME, 'moneyAmount')
        amount.send_keys(price)

        create = driver.find_element(By.CLASS_NAME, 'Button-module__content_kpdCF')
        create.click()

        time.sleep(4)

def pay_conf(price):
    global c
    c = False
    options = Options()
    options.add_argument("user-data-dir=/home/sergey/SeleniumProfile")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://www.tinkoff.ru/summary/')
    time.sleep(3)
    try:
        element = driver.find_element(By.ID, "pinCodeField")
        if element:
            pin1 = driver.find_element(By.ID, 'pinCode0')
            pin2 = driver.find_element(By.ID, 'pinCode1')
            pin3 = driver.find_element(By.ID, 'pinCode2')
            pin4 = driver.find_element(By.ID, 'pinCode3')
            #и пин код не солью тоже
            pin1.send_keys('X')
            pin2.send_keys('X')
            pin3.send_keys('X')
            pin4.send_keys('X')


    except NoSuchElementException:
        element = driver.find_element(By.CLASS_NAME, 'Money--module__money_a1HkQy')
        t = element.text
        t = t.replace('\n', '')
        if str(t) == '+'+str(price):
            c = True
    else:
        element = driver.find_element(By.CLASS_NAME, 'Money--module__money_a1HkQy')
        t = element.text
        t = t.replace('\n', '')
        if str(t) == '+'+str(price):
            c = True
