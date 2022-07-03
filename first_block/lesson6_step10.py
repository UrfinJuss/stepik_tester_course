from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first").send_keys('Name')
    browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second").send_keys('Family')
    browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third").send_keys('email@email.email')


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(2)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
