import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest_check as check


@pytest.fixture()
def test_setup_and_teardown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

    yield driver

    driver.quit()


def test_validProduct(test_setup_and_teardown):
    driver = test_setup_and_teardown

    driver.find_element(By.XPATH, '//*[@id="search"]/input').send_keys("HP")
    driver.find_element(By.XPATH, '//*[@id="search"]/span/button').click()

    check.is_true(False,"Intentional failure for testing")
    print("Product found")


def test_invalidProduct(test_setup_and_teardown):
    driver = test_setup_and_teardown

    driver.find_element(By.XPATH, '//*[@id="search"]/input').send_keys("hdfg")
    driver.find_element(By.XPATH, '//*[@id="search"]/span/button').click()

    check.is_true(driver.find_element(By.XPATH,'//*[@id="content"]/p[2]').is_displayed(),"Warning message is not displayed")

    print("Product not found")


def test_noProduct(test_setup_and_teardown):
    driver = test_setup_and_teardown

    driver.find_element(By.XPATH, '//*[@id="search"]/span/button').click()

    check.equal(driver.find_element(By.XPATH,'//*[@id="input-search"]').get_attribute("value"),"","Search field is not empty")

    print("No product entered")