# переключаемся на предупреждение
alert = browser.switch_to.alert
# соглашаемся с ним
alert.accept()

# так можно получить текст
alert_text = alert.text

# при модальном окне можно нажать отменя
confirm = browser.switch_to.alert
confirm.dismiss()

# Модальное окно где просят ввести текст
prompt = browser.switch_to.alert
prompt.send_keys("My answer")
prompt.accept()