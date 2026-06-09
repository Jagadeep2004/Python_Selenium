from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationexercise.com")

assert "Automation Exercise" in driver.title

actions = ActionChains(driver)

footer_element = driver.find_element(By.ID,'susbscribe_email')
actions.scroll_to_element(footer_element).perform()

assert driver.find_element(By.XPATH,'//h2[text()="Subscription"]').is_displayed()

footer_element.send_keys("Butcher@gmail.com")

driver.find_element(By.ID,'subscribe').click()

assert driver.find_element(By.XPATH,'//div[@class="alert-success alert"]').is_displayed()

time.sleep(5)
