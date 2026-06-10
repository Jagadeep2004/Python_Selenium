from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage:
    search_bar = (By.XPATH,'//*[@id="search"]/input')
    search_button = (By.XPATH,'//*[@id="search"]/span/button')
    displayed_prod_name = (By.XPATH,'//*[@id="content"]/div[3]/div/div/div[2]/div[1]/h4/a')

    def __init__(self,driver):
        self.driver = driver