from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.leafground.com/select.xhtml;jsessionid=node0p0bws5xx2g2hw0icx68md0ln17900013.node0")

# tool_select = Select(driver.find_element(By.XPATH,"//select[@class='ui-selectonemenu']"))

# tool_select.select_by_index(1)
# tool_select.select_by_visible_text("Playwright")

# for i in tool_select.options:
#     print(i.text)

dropdown = driver.find_element(By.XPATH,'//*[@id="j_idt87:country"]/div[3]')
dropdown.click()

option = driver.find_element(By.XPATH,'//li[text()="India"]')
option.click()

time.sleep(5)