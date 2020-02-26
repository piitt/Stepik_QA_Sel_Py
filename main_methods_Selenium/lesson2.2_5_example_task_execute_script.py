from selenium import webdriver

link = "https://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)
button = browser.find_element_by_tag_name("button")

# заставляем браузер проскролить нужный элемент, чтобы он точно стал видимым
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)

#скролим всю страницу целиком на строго заданное количество пикселей
browser.execute_script("window.scrollBy(0, 300);")
button.click()
assert True
