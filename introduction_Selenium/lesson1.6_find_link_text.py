from selenium import webdriver
import math
from time import sleep

link = "http://suninjuly.github.io/find_link_text"
link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    f_link = browser.find_element_by_link_text(link_text)
    f_link.click()
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Alehandro")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Plaha")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Simfer")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    sleep(15)
    browser.quit()
