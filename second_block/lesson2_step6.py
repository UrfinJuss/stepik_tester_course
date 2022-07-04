from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

link = 'http://suninjuly.github.io/execute_script.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))



try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_elem = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_elem.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 150);")
    time.sleep(1)
    
    browser.find_element(By.CSS_SELECTOR, "[id='answer']").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']").click()
    browser.find_element(By.CSS_SELECTOR, "[id='robotsRule']").click()



    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
