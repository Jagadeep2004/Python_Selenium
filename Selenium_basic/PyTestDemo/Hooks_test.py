from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def setup_function(function):
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")


def teardown_function(function):
    driver.quit()


def test_valid_product():
    driver.find_element(By.NAME, "search").send_keys("HP")
    driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)
    assert driver.find_element(By.XPATH, "//a[text()='HP LP3065']").is_displayed, "The product is not displayed"

def test_invalid_product(self):
    self.driver.find_element(By.XPATH, "//input[@name = 'search']").send_keys("Honda")
    self.driver.find_element(By.XPATH, "//input[@name = 'search']").send_keys(Keys.ENTER)
    assert self.driver.find_element(By.XPATH, "//p[text() = \"There is no product that matches the search criteria.\"]").is_displayed(), "No product Message is not displayed"

def test_no_product(self):
    self.driver.find_element(By.XPATH, "//input[@name = 'search']").send_keys("")
    self.driver.find_element(By.XPATH, "//input[@name = 'search']").send_keys(Keys.ENTER)
    assert self.driver.find_element(By.XPATH, "//p[text() = \"There is no product that matches the search criteria.\"]").is_displayed(), "No product Message is not displayed"