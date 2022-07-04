import time, math

from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/redirect_accept.html'

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    browser.switch_to.window(browser.window_handles[1])
    
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    print(browser.switch_to.alert.text)
    
finally:
    browser.quit()
