import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    print("\nStart browser GoogleChome Local conftest")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser GoogleChome Local conftest")
    browser.quit()
