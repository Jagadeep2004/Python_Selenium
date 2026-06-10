import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Actions.searchActions import SearchActions
from Utilities.logCreater import log_generator

@pytest.mark.search()
def test_search(setup):
    logger = log_generator()

    logger.info("Entering product details")

    search_action = SearchActions(setup)

    search_action.search()

    assert search_action.assert_results("HP LP3065")

    logger.info("Products is present")