import unittest
from selenium import webdriver


class TestUniqueSelectors(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def test_unique_selector1(self):
        page_url1 = 'http://suninjuly.github.io/registration1.html'
        browser = self.browser
        browser.implicitly_wait(5)
        browser.maximize_window()
        browser.get(page_url1)
        # first name
        first_name = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
        first_name.send_keys("Alexandro")
        # last name
        last_name = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
        last_name.send_keys("Plaha")
        # email
        email = browser.find_element_by_class_name("third")
        email.send_keys("123@mail.ru")
        # clicl button submit
        browser.find_element_by_css_selector("button.btn").click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_unique_selector2(self):
        page_url1 = 'http://suninjuly.github.io/registration2.html'
        browser = self.browser
        browser.implicitly_wait(5)
        browser.maximize_window()
        browser.get(page_url1)
        # first name
        first_name = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
        first_name.send_keys("Alexandro")
        # last name
        last_name = browser.find_element_by_xpath("//input[@class='form-control second' and @required]")
        last_name.send_keys("Plaha")
        # email
        email = browser.find_element_by_class_name("third")
        email.send_keys("123@mail.ru")
        # click button submit
        browser.find_element_by_css_selector("button.btn").click()
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()
