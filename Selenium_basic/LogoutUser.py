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

try:

    driver = webdriver.Chrome();
    wait = WebDriverWait(driver, 10)

    driver.maximize_window();
    driver.get("https://automationexercise.com/")

    assert driver.title == "Automation Exercise", "Home page title mismatch"
    print("Home page is reached.")

    jsClick(waitForClickable((By.XPATH, "//a[@href = \"/login\"]")))
    
    assert waitForElement((By.XPATH, "//h2[text() = \"Login to your account\"]")).is_displayed(), "Login page is not reached"
    
    print("Login text is verified")
    waitForElement((By.XPATH, "//input[@data-qa = \"login-email\"]")).send_keys("bvetrivel1@gmail.com2")
    waitForElement((By.XPATH, "//input[@data-qa = \"login-password\"]")).send_keys("Vetri@1234")
    jsClick(waitForClickable((By.XPATH, "//button[@data-qa = \"login-button\"]")))

    assert waitForElement((By.XPATH, "//i/following-sibling::b")).text == "Vetri", "Cannot login"
    
    print("Login Successfull")
    jsClick(waitForClickable((By.XPATH, "//a[@href = \"/logout\"]")))

    assert waitForElement((By.XPATH, "//h2[text() = \"Login to your account\"]")).is_displayed(), "Login page is not reached"
    print("Account logged out successfully.")
    print("Test case passed.")
    
except Exception as e:
    print(f"Test Failed: {e}")
    raise

finally:
    driver.quit()