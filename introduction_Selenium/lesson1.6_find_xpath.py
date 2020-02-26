from selenium import webdriver
from time import sleep

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Alehandro")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Plaha")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Simfer")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()
finally:
    sleep(20)
    browser.quit()
