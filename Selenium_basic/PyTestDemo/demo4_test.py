from selenium import webdriver as wb
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import pytest

@pytest.mark.parametrize("browser", ["edge", "chrome"])
@pytest.mark.parametrize("url", ["https://www.flipkart.com", "https://www.amazon.com"])
def test_sample(browser, url):

    if browser == "chrome":
        options = ChromeOptions()
        # options.add_argument("--headless=new")
        driver = wb.Chrome(options=options)

    else:
        options = EdgeOptions()
        # options.add_argument("--headless=new")
        driver = wb.Edge(options=options)

    driver.get(url)

    print(driver.title)

    driver.quit()