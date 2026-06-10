from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.searchPage import SearchPage
from Utilities.read_config import get_config

class SearchActions:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
    
    prod = get_config("prod info","p_name")
    def sendProdName(self,prod):
        self.wait.until(EC.visibility_of_element_located(SearchPage.search_bar)).send_keys(prod)
    
    def clickSearch(self):
        self.wait.until(EC.element_to_be_clickable(SearchPage.search_button)).click()

    def search(self):
        self.sendProdName(self.prod)
        self.clickSearch()

    def assert_results(self,name):
       return self.wait.until(EC.visibility_of_element_located(SearchPage.displayed_prod_name)).text == name