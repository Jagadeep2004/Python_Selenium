import pytest
import configparser

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Actions.loginActions import LoginActions
from Utilities.excelReader import get_data
from Utilities.logCreater import log_generator

config = configparser.RawConfigParser()
config.read("./Utilities/config.ini")


@pytest.mark.parametrize("email,password",get_data("./ExcelFiles/login_data.xlsx", "valid_login"))
def test_login(setup, email, password):

    logger = log_generator()

    logger.info("Entering Email")

    login_action = LoginActions(setup)
    login_action.login(email, password)

    assert "account" in setup.current_url.lower()

    logger.info("Login Successful")