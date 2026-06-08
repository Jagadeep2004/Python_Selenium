from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://automationexercise.com")

assert "Automation Exercise" in driver.title

driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a').click()

actions = ActionChains(driver)

first_product = driver.find_element(By.XPATH, "(//div[@class='product-image-wrapper'])[1]")
actions.move_to_element(first_product).perform()

first_add_to_cart = driver.find_element(By.XPATH, "(//a[@data-product-id='1'])[1]")
driver.execute_script("arguments[0].click();", first_add_to_cart)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Continue Shopping']"))).click()

second_product = driver.find_element(By.XPATH, "(//div[@class='product-image-wrapper'])[2]")
actions.move_to_element(second_product).perform()

second_add_to_cart = driver.find_element(By.XPATH, "(//a[@data-product-id='2'])[1]")
driver.execute_script("arguments[0].click();", second_add_to_cart)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//u[text()='View Cart']"))).click()

products = driver.find_elements(By.XPATH, "//tr[contains(@id,'product-')]")
assert len(products) == 2

price1 = driver.find_element(By.XPATH, "//*[@id='product-1']//td[@class='cart_price']/p").text
qty1 = driver.find_element(By.XPATH, "//*[@id='product-1']//td[@class='cart_quantity']/button").text
total1 = driver.find_element(By.XPATH, "//*[@id='product-1']//td[@class='cart_total']/p").text

price2 = driver.find_element(By.XPATH, "//*[@id='product-2']//td[@class='cart_price']/p").text
qty2 = driver.find_element(By.XPATH, "//*[@id='product-2']//td[@class='cart_quantity']/button").text
total2 = driver.find_element(By.XPATH, "//*[@id='product-2']//td[@class='cart_total']/p").text

assert price1 == "Rs. 500"
assert qty1 == "1"
assert total1 == "Rs. 500"

assert price2 == "Rs. 400"
assert qty2 == "1"
assert total2 == "Rs. 400"

driver.quit()