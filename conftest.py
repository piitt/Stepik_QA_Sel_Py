import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    print("\nStart browser GoogleChome Global conftest")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser GoogleChome Global conftest")
    browser.quit()
