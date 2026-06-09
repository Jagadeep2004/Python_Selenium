import pytest
import configparser

from selenium.webdriver.common.by import By
from Utilities.excelReader import get_data
from Utilities.logCreater import log_generator

config = configparser.RawConfigParser()
config.read("./Utilities/config.ini")

@pytest.mark.parametrize("email,password",get_data("./ExcelFiles/login_data.xlsx", "valid_login"))
def test_login(setup, email, password):

    logger = log_generator()

    driver = setup

    logger.info("Opening TutorialsNinja Website")

    driver.get(config.get("common info", "baseURL"))

    driver.find_element(By.XPATH, "//span[text()='My Account']").click()

    driver.find_element(By.LINK_TEXT, "Login").click()

    logger.info(f"Entering Email : {email}")

    driver.find_element(By.ID, "input-email").send_keys(email)

    driver.find_element(By.ID, "input-password").send_keys(password)

    driver.find_element(By.XPATH, "//input[@value='Login']").click()

    assert "account" in driver.current_url.lower()

    logger.info("Login Successful")