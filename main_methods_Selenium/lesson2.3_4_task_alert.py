from selenium import webdriver
from time import sleep
from math import log, sin


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)
    browser.find_element_by_class_name("btn").click()
    browser.switch_to.alert.accept()
    var_x = calc(browser.find_element_by_id("input_value").text)
    browser.find_element_by_id("answer").send_keys(var_x)
    browser.find_element_by_class_name("btn").click()
finally:
    sleep(15)
    browser.quit()
