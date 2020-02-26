from selenium import webdriver

browser = webdriver.Chrome()

### выполнение сценария Javascript

# browser.execute_script("alert('Robots at work');")

# browser.execute_script("document.title='Script executing';")

browser.execute_script("document.title='Script executing'; alert('Robots at work');")
