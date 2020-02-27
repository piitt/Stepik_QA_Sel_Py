from selenium import webdriver
import os

# получаем путь к директории текущего исполняемого файла
current_dir_path = os.path.abspath(os.path.dirname(__file__))

# получаем путь к файлу
file_path = os.path.join(current_dir_path, 'file.txt')

# загружаем файл
element.send_keys(file_path)

