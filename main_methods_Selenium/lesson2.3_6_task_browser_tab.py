from selenium import webdriver
from time import sleep
from math import log, sin


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

with webdriver.Chrome() as browser:
    browser.maximize_window()
    browser.get(link)
    browser.find_element_by_xpath("//button[@class='trollface btn btn-primary']").click()
    browser.switch_to.window(browser.window_handles[1])
    var_x = calc(browser.find_element_by_id("input_value").text)
    browser.find_element_by_id("answer").send_keys(var_x)
    browser.find_element_by_class_name("btn").click()
    sleep(15)
