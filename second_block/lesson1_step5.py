from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = "http://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR, ".form-group .form-control").send_keys(y)
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']").click()
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    time.sleep(1)


    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()
    
