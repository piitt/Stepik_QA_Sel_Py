import os
from selenium import webdriver
from time import sleep

link = "http://suninjuly.github.io/file_input.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    browser.maximize_window()
    # путь к файлу
    current_dir_path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir_path, 'file.txt')
    # заполняем поля
    browser.find_element_by_xpath("//input[@name='firstname' and @required]").send_keys("Alehandro")
    browser.find_element_by_xpath("//input[@name='lastname' and @required]").send_keys("Plaha")
    browser.find_element_by_xpath("//input[@name='email' and @required]").send_keys("123.ya.ru")
    # загружаем файл
    browser.find_element_by_id("file").send_keys(file_path)
    # отправляем данные
    browser.find_element_by_class_name("btn").click()
    sleep(15)
