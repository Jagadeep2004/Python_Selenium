from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    account_icon = (By.XPATH,'//*[@id="top-links"]/ul/li[2]/a/i')
    login = (By.XPATH,'//*[@id="top-links"]/ul/li[2]/ul/li[2]/a')
    email = (By.ID, "input-email")
    password = (By.ID,"input-password")
    login_button = (By.XPATH,'//*[@id="content"]/div/div[2]/div/form/input')

    def __init__(self, driver):
        self.driver = driver