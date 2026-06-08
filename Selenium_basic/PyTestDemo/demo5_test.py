import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture()
def test_setup_and_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
    yield
    driver.quit()

def test_validProduct(test_setup_and_teardown):
    driver.find_element(By.XPATH,'//*[@id="search"]/input').send_keys("HP")
    driver.find_element(By.XPATH,'//*[@id="search"]/span/button').click()
    assert driver.find_element(By.XPATH,'//h2[text()="Products meeting the search criteria"]').is_displayed()
    print("Product found")

def test_invalidProduct(test_setup_and_teardown):
    driver.find_element(By.XPATH,'//*[@id="search"]/input').send_keys("hdfg")
    driver.find_element(By.XPATH,'//*[@id="search"]/span/button').click()
    assert driver.find_element(By.XPATH,'//*[@id="content"]/p[2]').is_displayed()
    print("Product not found")

def test_noProduct(test_setup_and_teardown):
    driver.find_element(By.XPATH,'//*[@id="search"]/span/button').click()
    assert driver.find_element(By.XPATH,'//*[@id="input-search"]').get_attribute("value") == ""
    print("No product entered")