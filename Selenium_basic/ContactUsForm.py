from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://automationexercise.com")

assert "Automation Exercise" in driver.title
print("Home page is visible successfully")

contact_us_button = driver.find_element(By.XPATH,'//a[@href="/contact_us"]').click()

WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//h2[text()="Get In Touch"]')))

assert driver.find_element(By.XPATH,'//h2[text()="Get In Touch"]').text == "GET IN TOUCH"

name = driver.find_element(By.XPATH,'//input[@name="name"]')
name.send_keys("Butcher")

email = driver.find_element(By.XPATH,'//input[@name="email"]')
email.send_keys("butcher@gmail.com")

sub = driver.find_element(By.XPATH,'//input[@name="subject"]')
sub.send_keys("Leave")

msg = driver.find_element(By.XPATH,'//textarea[@id = "message"]')
msg.send_keys("Hello all")

driver.find_element(By.XPATH,'//input[@name="submit"]').click()

WebDriverWait(driver,10).until(EC.alert_is_present())
alert = driver.switch_to.alert

alert.accept()