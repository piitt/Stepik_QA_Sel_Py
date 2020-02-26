from selenium import webdriver
from time import sleep
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

with webdriver.Chrome() as browser:
    browser.maximize_window()
    browser.get(link)
    var_x = calc(browser.find_element_by_id("input_value").text)
    search = browser.find_element_by_id("answer")
    search.send_keys(var_x)
    ch_box = browser.find_element_by_id("robotCheckbox")
    ch_box.click()
    r_btn = browser.find_element_by_id("robotsRule")
    r_btn.click()
    submit_btn = browser.find_element_by_class_name("btn")
    submit_btn.click()
    sleep(15)