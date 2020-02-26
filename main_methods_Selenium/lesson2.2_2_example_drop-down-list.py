from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://ya.ru")

# найти выпадающий список и кликнуть на него
browser.find_element_by_tag_name("select").click()
browser.find_element_by_css_selector("option:nth-child(2)").click()
# или так
browser.find_element_by_css_selector("[value='1']").click()

# Более удобный способ
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value("1")
# найти элемент по видимому тексту
select.select_by_visible_text("text")
# найти элемент по индексу или порядковому номеру
select.select_by_index(1)
