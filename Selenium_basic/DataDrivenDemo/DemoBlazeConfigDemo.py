import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from read_config import get_config

@pytest.mark.usefixtures("driver")
class TestLogin:
    def test_login(self):
        username = get_config("login info","username")
        password = get_config("login info","password")
        wait = WebDriverWait(self.driver,10)

        self.driver.find_element(By.XPATH,'//*[@id="login2"]').click()
        wait.until(EC.visibility_of_element_located((By.ID,'loginusername')))

        self.driver.find_element(By.ID,'loginusername').send_keys(username)
        self.driver.find_element(By.ID,'loginpassword').send_keys(password)
        self.driver.find_element(By.XPATH,'//*[@id="logInModal"]/div/div/div[3]/button[2]').click()

        wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="nameofuser"]')))
        assert self.driver.find_element(By.XPATH,'//*[@id="nameofuser"]').text == "Welcome ronaldo007"
        print("Login Successful")


