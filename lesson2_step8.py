from selenium import webdriver
from selenium.webdriver.common.by import By
import os, time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'
browser.get(link)

try:
    browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('Paul')
    browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('Zabolotnyi')
    browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('By_pa@icloud.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    browser.find_element(By.CSS_SELECTOR, '[type="file"]').send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
finally:
    time.sleep(5)
    browser.quit()
 
