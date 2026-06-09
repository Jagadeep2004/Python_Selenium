from selenium import webdriver
from read_config import get_config
import pytest

@pytest.fixture()
def driver(request):
    browser = get_config("basic info","browser")
    if browser == "Chrome":
        driver = webdriver.Chrome()
    driver.maximize_window()
    url = get_config("basic info","url")
    driver.get(url)
    request.cls.driver = driver
    yield driver
    driver.quit()