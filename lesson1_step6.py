from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = 'http://suninjuly.github.io/get_attribute.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_elem = browser.find_element(By.CSS_SELECTOR, "[id='treasure']")
    x = x_elem.get_attribute("valuex")
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR, "[id='answer']").send_keys(y)
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']").click()
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']").click()
    time.sleep(1)


    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
