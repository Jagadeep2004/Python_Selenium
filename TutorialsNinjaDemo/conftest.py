import pytest
import configparser
from selenium import webdriver

config = configparser.RawConfigParser()
config.read("./Utilities/config.ini")

@pytest.fixture()
def setup():

    browser = config.get("common info", "browser")

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()

    elif browser.lower() == "edge":
        driver = webdriver.Edge()

    else:
        driver = webdriver.Firefox()

    driver.get(config.get("common info", "baseURL"))

    driver.maximize_window()

    yield driver

    driver.quit()