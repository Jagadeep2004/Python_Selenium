from Pages.loginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginActions:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_account_icon(self):
        self.wait.until(EC.element_to_be_clickable(LoginPage.account_icon)).click()

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(LoginPage.login)).click()

    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located(LoginPage.email)).send_keys(email)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(LoginPage.password)).send_keys(password)

    def click_login_button(self):
        self.wait.until(EC.element_to_be_clickable(LoginPage.login_button)).click()

    def login(self, email, password):
        self.click_account_icon()
        self.click_login()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()