from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.set_window_size(1400, 900)
browser.get('http://www.baidu.com')

input = browser.find_element(By.ID, 'kw')
input.send_keys('ipad')
time.sleep(5)
input.clear()

input.send_keys('吴亦凡')
button = browser.find_element(By.ID, 'su')
button.click()
time.sleep(10)
browser.quit()
