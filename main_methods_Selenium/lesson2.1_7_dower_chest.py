from selenium import webdriver
from time import sleep
from math import log, sin


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

with webdriver.Chrome() as browser:
    browser.maximize_window()
    browser.get(link)
    # находим кртинку-сундук
    img_chest = browser.find_element_by_id("treasure")
    # получаем заначение аттрибута и производим рассчет
    var_x = calc(img_chest.get_attribute("valuex"))
    # находим пле для ввода
    search = browser.find_element_by_id("answer")
    # всталяем значение
    search.send_keys(var_x)
    # находим чекбокс и кликаем
    im_robot = browser.find_element_by_id("robotCheckbox")
    im_robot.click()
    # находим радиокнопку и кликаем
    robots_rule = browser.find_element_by_id("robotsRule")
    robots_rule.click()
    # находим кнопку отправить и отправляем
    submit_btn = browser.find_element_by_class_name("btn")
    submit_btn.click()
    sleep(15)
