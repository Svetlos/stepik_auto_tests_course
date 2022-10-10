from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

# открытие страницы
link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    WebDriverWait(browser, "12").until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))   
    btn = browser.find_element(By.ID,"book")
    btn.click() 
    
    #Пройти капчу для робота и получить число-ответ
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    print (x)
    
    y = calc(int(x))
    print(y)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()