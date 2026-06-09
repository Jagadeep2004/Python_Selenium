from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def waitForElement(locator):
    return wait.until(EC.visibility_of_element_located(locator))

def waitForClickable(locator):
    return wait.until(EC.element_to_be_clickable(locator))

def jsClick(element):
    driver.execute_script("arguments[0].click();",element)

driver=webdriver.Chrome()
driver.maximize_window()

wait=WebDriverWait(driver, 15)

driver.get("https://automationexercise.com/")

header=waitForElement((By.XPATH, "//*[@id='header']/div/div/div"))

if (header.is_displayed()):
    print("Home displayed")
else:
    print("Home not displayed")

signupButton=waitForClickable((By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a"))
jsClick(signupButton)

name=waitForElement((By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[2]"))

email=waitForElement((By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/input[3]"))

if (name.is_enabled()):
    name.send_keys("Ronaldo")
    email.send_keys("cr7@gmail.com")

signupCreateButton=waitForClickable((By.XPATH, "//*[@id='form']/div/div/div[3]/div/form/button"))
jsClick(signupCreateButton)

password=waitForElement((By.ID,"password"))
firstName=waitForElement((By.ID,"first_name"))
lastName=waitForElement((By.ID,"last_name"))
state=waitForElement((By.ID,"state"))
city=waitForElement((By.ID,"city"))
zipCode=waitForElement((By.ID,"zipcode"))
phone=waitForElement((By.ID,"mobile_number"))
address=waitForElement((By.ID,"address1"))

firstName.send_keys("Ronaldo")
lastName.send_keys("c")
password.send_keys("admin")
state.send_keys("TamilNadu")
city.send_keys("Mettur Dam")
address.send_keys("Indira nagar")
zipCode.send_keys("636401")
phone.send_keys("9677558855")

createAccountButton = waitForClickable((By.XPATH, "//*[@id='form']/div/div/div/div[1]/form/button"))
jsClick(createAccountButton)

accountCreated = waitForElement((By.XPATH, "//b[text()='Account Created!']"))

if (accountCreated.is_displayed()):
    print("Account created.")
else:
    print("Account didnt created.")

continueButton=waitForClickable((By.XPATH, "//*[@id='form']/div/div/div/div/a"))
jsClick(continueButton)

deleteButton=waitForClickable((By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a"))
jsClick(deleteButton)

accountDeleted=waitForElement((By.XPATH, "//*[@id='form']/div/div/div/h2"))

if (accountDeleted.is_displayed()):
    print("Account Deleted.")
else:
    print("Account didnt Deleted.")

driver.quit()