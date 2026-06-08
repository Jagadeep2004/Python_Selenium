import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.mark.parametrize("search_term",["selenium", "pytest", "selenium locators"]
)
def test_search(search_term):
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.google.com")

    search_bar = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.ENTER)

    driver.quit()