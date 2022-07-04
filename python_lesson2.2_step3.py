from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    number1_element = browser.find_element(By.CSS_SELECTOR, "#num1")
    number2_element = browser.find_element(By.CSS_SELECTOR, "#num2")
    number1 = int(number1_element.text)
    number2 = int(number2_element.text)
    int_sum = number1 + number2
    str_sum = str(int_sum)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str_sum)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()