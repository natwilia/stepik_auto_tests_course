from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("James")
    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Holden")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("James.Holden@test.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "bio.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "#file")
    element.send_keys(file_path)    
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()