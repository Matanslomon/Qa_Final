import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests

# driver = webdriver.Chrome()
# url = 'https://www.saucedemo.com/'
# driver.maximize_window()


def open_site(driver, url):
    driver.get(url)
    time.sleep(3)
    return driver.current_url


def signin(driver, username, password):
    name = driver.find_element(By.CSS_SELECTOR, '#user-name')
    name.send_keys('standard_user')
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    password.send_keys('secret_sauce')
    time.sleep(4)
    button = driver.find_element(By.CSS_SELECTOR, '#login-button')
    button.click()
    time.sleep(3)
    return driver.current_url


def count_match(driver):
    add_button1 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
    add_button1.click()
    time.sleep(2)
    add_button2 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bike-light')
    add_button2.click()
    time.sleep(2)
    cart = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a')
    cart.click()
    time.sleep(2)
    checkout = driver.find_element(By.CSS_SELECTOR, '#checkout')
    checkout.click()
    time.sleep(2)
    firstname_box = driver.find_element(By.CSS_SELECTOR, '#first-name')
    firstname_box.send_keys('mati')
    lastname_box = driver.find_element(By.CSS_SELECTOR, '#last-name')
    lastname_box.send_keys('sol')
    zip_box = driver.find_element(By.CSS_SELECTOR, '#postal-code')
    zip_box.send_keys('9664')
    button_continue = driver.find_element(By.CSS_SELECTOR, '#continue')
    button_continue.click()
    time.sleep(2)
    number = driver.find_element(By.CSS_SELECTOR,
                                 '#checkout_summary_container > div > div.summary_info > div.summary_info_label.summary_total_label')
    number = number.text
    return float(number[-5:])


def complete_test(driver):
    add_Sauce_Labs_Onesie = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')
    add_Sauce_Labs_Onesie.click()
    time.sleep(2)
    cart = driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container > a')
    cart.click()
    time.sleep(2)
    checkout = driver.find_element(By.CSS_SELECTOR, '#checkout')
    checkout.click()
    time.sleep(2)
    firstname_box = driver.find_element(By.CSS_SELECTOR, '#first-name')
    firstname_box.send_keys('mati')
    lastname_box = driver.find_element(By.CSS_SELECTOR, '#last-name')
    lastname_box.send_keys('sol')
    zip_box = driver.find_element(By.CSS_SELECTOR, '#postal-code')
    zip_box.send_keys('9664')
    button_continue = driver.find_element(By.CSS_SELECTOR, '#continue')
    button_continue.click()
    time.sleep(2)
    finish = driver.find_element(By.CSS_SELECTOR, '#finish')
    finish.click()
    time.sleep(2)
    return driver.current_url


def price_order(driver):
    order_button = driver.find_element(By.CSS_SELECTOR,'#header_container > div.header_secondary_container > div > span > select > option:nth-child(4)')
    order_button.click()
    time.sleep(4)
    image_1 = driver.find_element(By.CSS_SELECTOR,'#inventory_container > div > div:nth-child(1) > div.inventory_item_description > div.pricebar > div')
    image_1 = image_1.text
    return float(image_1[-5:])
    time.sleep(2)
    image_2 = driver.find_element(By.CSS_SELECTOR,'#inventory_container > div > div:nth-child(6) > div.inventory_item_description > div.pricebar > div')
    image_2 = image_2.text
    return float(image_2[-4:])
    time.sleep(4)
    if image_1 > image_2:
        print('pass')
        return float(image_1[-5])




def send_http_request(url):
    res = requests.get(url)
    return res


def check_status_code(code):
    if 200 <= code < 400:
        print(f"success -->  {code}")
        return True
    else:
        print('error')
        return False


def check_word(url):
    res = requests.get(url)
    word = res.json()[0]

    if 'dʒɔɪ' in word['phonetic']:
        print(word['phonetic'])
        return True
    else:
        print('error')
        return False


