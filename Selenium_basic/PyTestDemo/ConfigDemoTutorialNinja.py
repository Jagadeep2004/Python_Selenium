import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from read_config import get_config


@pytest.fixture()
def test_setup_and_teardown():
    browser = get_config("basic info", "browser")

    global driver

    if browser.lower() == "chrome":
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get(get_config("basic info", "url"))

    yield

    driver.quit()


def test_validProduct(test_setup_and_teardown):
    driver.find_element(By.XPATH,'//*[@id="search"]/input').send_keys(get_config("product info", "valid_product"))

    driver.find_element(By.XPATH,'//*[@id="search"]/span/button').click()

    assert driver.find_element(By.XPATH,'//h2[text()="Products meeting the search criteria"]').is_displayed()

    print("Product found")


