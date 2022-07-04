from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)

try:
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    confim = browser.switch_to.alert
    confim.accept()
    
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    
    browser.find_element(By.ID, 'answer').send_keys(y)
    
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
finally:
    time.sleep(5)
    browser.quit()
 
