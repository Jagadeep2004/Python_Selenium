from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationexercise.com")

assert "Automation Exercise" in driver.title
print("Home page is visible successfully")

driver.find_element(By.LINK_TEXT, "Signup / Login").click()

assert driver.find_element(By.XPATH, "//h2[text()='Login to your account']").is_displayed()
print("Login to your account is visible")

driver.find_element(By.XPATH, "//input[@data-qa='login-email']").send_keys("Butcher@gmail.com")

driver.find_element(By.XPATH, "//input[@data-qa='login-password']").send_keys("admin")

driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()

assert driver.find_element(By.XPATH, "//a[contains(text(),'Logged in as')]").is_displayed()
print("Logged in successfully")

driver.find_element(By.XPATH, "//a[contains(text(),'Delete Account')]").click()

time.sleep(5)



time.sleep(3)
driver.quit()
