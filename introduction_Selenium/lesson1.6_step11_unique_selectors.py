from selenium import webdriver
from time import sleep

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link2)
    # first name
    input1 = browser.find_element_by_xpath("//input[@class='form-control first' and @required]")
    input1.send_keys("Alexandro")
    # last name
    input2 = browser.find_element_by_css_selector("input[placeholder='Input your last name']")
    input2.send_keys("Plaha")
    # email
    input3 = browser.find_element_by_class_name("third")
    input3.send_keys("123@mail.ru")
    # button submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    sleep(10)
    browser.quit()
