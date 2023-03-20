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


    def test_sanity(self,driver,url):
        expected = url
        actual = open_site(driver,expected)
        assert expected == actual


    @pytest.mark.parametrize('username,password',[ ('standard_user','secret_sauce'),('slomon','matan12') ])
    def test_login(self,driver,url,username,password):
        expected = 'https://www.saucedemo.com/inventory.html'
        open_site(driver,url)
        actual = signin(driver, username , password )
        assert actual == expected











