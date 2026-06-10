import pytest
import configparser

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.excelReader import get_data
from Utilities.logCreater import log_generator

config = configparser.RawConfigParser()
config.read("./Utilities/config.ini")


@pytest.mark.parametrize("email,password",get_data("./ExcelFiles/login_data.xlsx", "valid_login"))
def test_login(setup, email, password):

    logger = log_generator()

    driver = setup

    wait = WebDriverWait(driver, 20)

    logger.info("Opening TutorialsNinja Website")

    driver.get(config.get("common info", "baseURL"))

    wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='top-links']//span[contains(text(),'My Account')]"))).click()

    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()

    logger.info(f"Entering Email : {email}")

    wait.until(EC.visibility_of_element_located((By.ID, "input-email"))).send_keys(email)

    driver.find_element(By.ID, "input-password").send_keys(password)

    driver.find_element(By.XPATH,"//input[@value='Login']").click()

    wait.until(EC.url_contains("account"))

    assert "account" in driver.current_url.lower()

    logger.info("Login Successful")