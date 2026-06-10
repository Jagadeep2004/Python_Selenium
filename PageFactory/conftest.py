import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def setup_tearDown(request):

    driver = webdriver.Chrome()
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    driver.get("https://tutorialsninja.com/demo/")

    request.cls.driver = driver
    request.cls.wait = wait

    yield

    driver.quit()