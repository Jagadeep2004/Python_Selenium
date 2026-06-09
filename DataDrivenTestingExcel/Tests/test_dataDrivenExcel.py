import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities import excelReader
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.logCreater import log_generator


@pytest.mark.parametrize(
    "username,password",
    excelReader.get_data("ExcelFiles/login_data.xlsx", "login")
)
class TestLogin1:

    def test_validLogin(self, username, password):

        logger = log_generator()

        logger.info("Launching Chrome Browser")

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        logger.info("Opening Demoblaze Application")

        self.driver.get("https://www.demoblaze.com/index.html")

        wait = WebDriverWait(self.driver, 20)

        logger.info("Clicking Login Link")

        self.driver.find_element(By.ID, "login2").click()

        wait.until(EC.visibility_of_element_located((By.ID, "loginusername")))

        logger.info(f"Entering Username : {username}")

        self.driver.find_element(By.ID, "loginusername").send_keys(username)

        logger.info("Entering Password")

        self.driver.find_element(By.ID, "loginpassword").send_keys(password)

        logger.info("Clicking Login Button")

        self.driver.find_element(By.XPATH,'//*[@id="logInModal"]/div/div/div[3]/button[2]').click()

        wait.until(EC.visibility_of_element_located((By.ID, "nameofuser")))

        actual_text = self.driver.find_element(By.ID,"nameofuser").text

        logger.info(f"Actual Welcome Message : {actual_text}")

        assert actual_text == f"Welcome {username}"

        logger.info("Login Successful")

        self.driver.quit()

        logger.info("Browser Closed")