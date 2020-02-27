from selenium import webdriver
from time import sleep
from math import log, sin


def calc(x):
    return str(log(abs(12 * sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)
    # получаем значение х
    var_x = calc(browser.find_element_by_id("input_value").text)
    # скролим страницу
    # browser.execute_script("arguments[0].scrollIntoView(true);", btn_submit)
    browser.execute_script("window.scrollBy(0, 150)")
    # находим поисковое поле и вставляем значение х
    browser.find_element_by_id("answer").send_keys(var_x)
    # отмечаем чекбокс
    browser.find_element_by_id("robotCheckbox").click()
    # отмечаем радиокнопку
    browser.find_element_by_id("robotsRule").click()
    # находим кнопку submit и кликаем
    btn_submit = browser.find_element_by_class_name("btn").click()
finally:
    sleep(15)
    browser.quit()

# from selenium.webdriver.common.action_chains import ActionChains
# ActionChains(driver).move_to_element(driver.sl.find_element_by_id('my-id')).perform()