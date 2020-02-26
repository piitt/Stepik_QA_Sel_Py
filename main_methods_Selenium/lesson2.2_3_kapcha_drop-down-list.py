from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep


def summma(a, b):
    return int(a) + int(b)


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)
    # находим первое число
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    # суммируем их
    var_s = summma(num1, num2)
    # выбираем вариант ответа из выпадающего списка
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(var_s))
    # отправляем данные
    browser.find_element_by_class_name("btn").click()
finally:
    sleep(15)
    browser.quit()
