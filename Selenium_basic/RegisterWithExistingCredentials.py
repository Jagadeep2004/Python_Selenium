from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://automationexercise.com")

assert "Automation Exercise" in driver.title

signup_button = driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
signup_button.click()

signuppage_verification_text = driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/h2')
assert "New User Signup!" in signuppage_verification_text.text

signup_name = driver.find_element(By.NAME,'name')
signup_name.send_keys('Butcher')

signup_email = driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/input[3]')
signup_email.send_keys('Butcher@gmail.com')

signup_button = driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/button')
signup_button.click()

assert "Email Address already exist!" in driver.find_element(By.XPATH,'//*[@id="form"]/div/div/div[3]/div/form/p').text
print("Asserted successfully")