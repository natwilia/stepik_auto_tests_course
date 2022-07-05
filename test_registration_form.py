import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegistrationForm(unittest.TestCase):
    def test_registration_form1(self):
        try: 
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
            input1.send_keys("James")
            input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
            input2.send_keys("Holden")
            input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
            input3.send_keys("test@test.com")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
                
            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be text 'Congratulations! You have successfully registered!'")

        finally:
            time.sleep(10)
            browser.quit()
                
    def test_registration_form2(self):
        try: 
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
            input1.send_keys("James")
            input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
            input2.send_keys("Holden")
            input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
            input3.send_keys("test@test.com")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
                
            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text

            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be text 'Congratulations! You have successfully registered!'")

        finally:
            time.sleep(10)
            browser.quit()   

if __name__ == "__main__":
    unittest.main()            