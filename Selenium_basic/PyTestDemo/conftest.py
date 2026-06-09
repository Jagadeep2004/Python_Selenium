from selenium import webdriver
import pytest


@pytest.fixture(params=["Chrome","Edge"])
def driver(request):
    if request.param == "Chrome":
        driver = webdriver.Chrome()
    elif request.param == "Edge":
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver = driver
    yield driver
    driver.quit()