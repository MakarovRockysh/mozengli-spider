# encoding: utf-8
from selenium import webdriver
import os
import time

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(1)
try:
    driver.get("https://www.bilibili.com/")
    driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/div[2]/div[1]/div[1]/form[1]/input[1]").send_keys('我的英雄学院')
    driver.find_element_by_class_name('search-submit').submit()
    windows = driver.current_window_handle
    all_handles = driver.window_handles
    for handle in all_handles:
        if handle != windows:
            driver.switch_to.window(handle)
    driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[2]/ul[1]/li[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/ul[1]/li[14]/a").click()
finally:
    os.system('taskkill /F /IM chromedriver.exe')
    # os.system('taskkill /F /IM chrome.exe')
