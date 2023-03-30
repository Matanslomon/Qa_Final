import pytest
from main import *
from selenium import webdriver


class TestSite:
    @pytest.fixture
    def driver(self):
        driver = webdriver.Chrome()
        return driver

    @pytest.fixture
    def url(self):
        return 'https://www.saucedemo.com/'

    def test_sanity(self, driver, url):
        expected = url
        actual = open_site(driver, expected)
        assert expected == actual

    # -------------- sanity test ------------------------------------------------------------------#

    # ----------------- login test --------------------------------------------------#
    @pytest.mark.parametrize('username,password', [('standard_user', 'secret_sauce')])
    def test_login(self, driver, url, username, password):
        expected = 'https://www.saucedemo.com/inventory.html'
        open_site(driver, url)
        actual = signin(driver, username, password)
        assert actual == expected

    # ----------------------- login test ------------------------------------------------------#

    # -------------------------total price ---------------------------------------------------#

    def test_count(self, driver, url):
        expected = 43.18
        open_site(driver, url)
        signin(driver, 'standard_user', 'secret_sauce')
        actual = count_match(driver)
        assert actual == expected

    # -------------------------total price ---------------------------------------------------#

    # --------------------- complete test ----------------------------------------------------#

    def test_complete_purchase(self, driver, url):
        expected = 'https://www.saucedemo.com/checkout-complete.html'
        open_site(driver, url)
        signin(driver, 'standard_user', 'secret_sauce')
        actual = complete_test(driver)
        assert actual == expected

# --------------------- complete test --------------------------------------#

#----------------------- high to low -----------------------------------------#

    def test_high_to_low(self,driver,url):
        expected = 49.99
        open_site(driver,url)
        signin(driver, 'standard_user', 'secret_sauce')
        actual = price_order(driver)
        assert actual == expected










class TestApi:

    def test_status_code(self):
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en/ignore'
        res = send_http_request(url)
        assert check_status_code(res.status_code) == True


    def test_check_word(self):
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en/joy'
        res = send_http_request(url)
        assert check_word(url) == True
