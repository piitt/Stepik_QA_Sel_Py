from selenium import webdriver

link = "http://suninjuly.github.io/math.html"

with webdriver.Chrome() as browser:
    browser.maximize_window()
    browser.get(link)
    # проверяем значение атрибута радиокнопки
    people_rule = browser.find_element_by_id("peopleRule")
    people_checked = people_rule.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    # проверяем значение атрибута радиокнопки
    robots_rule = browser.find_element_by_id("robotsRule")
    robots_checked = robots_rule.get_attribute("checked")
    print("value of robots radio: ", robots_checked)
    assert robots_checked is None
