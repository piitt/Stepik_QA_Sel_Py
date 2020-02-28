# явное ожидание
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait2.html")
# настраиваем ожидание 5c пока кнопка станет кликабельной
button = WebDriverWait(browser, 5).until(
    EC.element_to_be_clickable((By.ID, "verify"))
)
button.click()
message = browser.find_element_by_id("verify_message")
assert "successful" in message.text

# метод until_not инвертирует
# настраиваем ожидание 5c пока кнопка станет НЕ кликабельной
# wait = WebDriverWait(browser, 5)
# button = wait.until_not(EC.element_to_be_clickable((By.ID, "verify")))
browser.quit()
