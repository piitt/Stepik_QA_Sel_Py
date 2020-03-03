import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    @pytest.mark.smoke
    @pytest.mark.win10
    def test_guest_should_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".btn")

# запустить тесты с маркировкой regression
# pytest -s -v -m regression test_fixture8_mark.py

# запустить тесты которые без отметки smoke
# pytest -s -v -m "not smoke" test_fixture8_mark.py

# Объединение тестов с разными маркировками
# pytest -s -v -m "smoke or regression" test_fixture8_mark.py

# Выбор тестов, имеющих несколько маркировок
# pytest -s -v -m "smoke and win10" test_fixture81.py