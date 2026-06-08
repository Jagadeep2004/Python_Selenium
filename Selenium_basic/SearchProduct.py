from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://automationexercise.com")

assert "Automation Exercise" in driver.title

product_button = driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a')
product_button.click()

search_text_area = driver.find_element(By.ID,'search_product')
search_text_area.send_keys("shirts")

driver.find_element(By.ID,'submit_search').click()

assert driver.find_element(By.XPATH,'/html/body/section[2]/div/div/div[2]').is_displayed()

print("Products is displayed")
