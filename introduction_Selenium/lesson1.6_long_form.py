from selenium import webdriver
from time import sleep

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)
    #elements = browser.find_elements_by_xpath("//input[@type='text']")
    elements = browser.find_elements_by_css_selector("input[type = 'text']")
    for element in elements:
        element.send_keys("LONG")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    sleep(20)
    browser.quit()
