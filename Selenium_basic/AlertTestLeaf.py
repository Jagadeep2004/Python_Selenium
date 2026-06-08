from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.leafground.com/alert.xhtml")

simple_alert = driver.find_element(By.XPATH,'//*[@id="j_idt88:j_idt91"]/span[2]')
simple_alert.click()
print("Clicked")

WebDriverWait(driver,10).until(EC.alert_is_present())
print("Alert is present")
alert = driver.switch_to.alert

alert.accept()
print("alert accepted")
print()

confirmation_alert = driver.find_element(By.XPATH,'//*[@id="j_idt88:j_idt93"]/span[2]')
confirmation_alert.click()
print("alert clicked")
WebDriverWait(driver,10).until(EC.alert_is_present())
print("alert is present")
alert.dismiss()
print("alert is dismissed")
print()

prompt_alert =driver.find_element(By.XPATH,'//*[@id="j_idt88:j_idt104"]/span[2]')
prompt_alert.click()
print("alert clicked")
WebDriverWait(driver,10).until(EC.alert_is_present())
print("alert if present")
alert.send_keys("OK")
print("prompt is sent")
alert.accept()
print("alert accepted") 
