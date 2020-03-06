import pytest
from math import log
from time import time
from selenium import webdriver


@pytest.fixture
def browser():
    print("\nStart Broswer GoogleChrome")
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser. implicitly_wait(10)
    yield browser
    print("\nQuit Browser")
    browser.quit()


@pytest.mark.parametrize('var', ['6895', '6896', '6897', '6898', '6899', '6903', '6904', '6905'])
def test_answer(browser, var):
    link = f'https://stepik.org/lesson/23{var}/step/1'
    answer = str(log(int(time())))
    browser.get(link)
    browser.find_element_by_id("ember68").send_keys(answer)
    browser.find_element_by_class_name("submit-submission").click()
    string = browser.find_element_by_class_name("smart-hints__hint").text
    assert 'Correct!' == string
