from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin
from time import sleep


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)
    browser.implicitly_wait(5)
    wait = WebDriverWait(browser, 12)
    price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book = browser.find_element_by_id("book").click()
    var_x = calc(browser.find_element_by_id("input_value").text)
    answer = browser.find_element_by_id("answer")
    browser.execute_script("arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(var_x)
    solve = browser.find_element_by_id("solve").click()
finally:
    sleep(15)
    browser.quit()
