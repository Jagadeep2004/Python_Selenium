from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

def waitForElement(locator):
    return wait.until(EC.visibility_of_element_located(locator))

def waitForClickable(locator):
    return wait.until(EC.element_to_be_clickable(locator))

def jsClick(element):
    driver.execute_script("arguments[0].click();",element)

try:
    driver=webdriver.Chrome();
    wait=WebDriverWait(driver, 10)
    
    driver.maximize_window();
    driver.get("https://automationexercise.com/")

    assert driver.title=="Automation Exercise", "Home page title mismatch"
    print("Home page is reached.")

    waitForElement((By.XPATH,"//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a")).click()

    assert "test_cases" in driver.current_url

    print("Test cases page loaded")
    print("Test case successfull")

except Exception as e:
    print(e)