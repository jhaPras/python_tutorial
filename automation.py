import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import  BeautifulSoup

browser = webdriver.Chrome('/usr/local/bin/chromedriver 2')
page = browser.get('https://www.facebook.com/login')

username = browser.find_element_by_name('email').send_keys('prasen.jha')
password = browser.find_element_by_name('pass').send_keys('prasenjit@2211')

browser.find_element_by_id('loginbutton').click()


browser.find_element_by_name('xhpc_message').send_keys('just a post written by my bot ! if you think it\'s cool give a thumbs up')
WebDriverWait(browser,5)
browser.find_element_by_class_name('_1se_').click()
WebDriverWait(browser,10)
browser.find_element_by_class_name('_1mf7 _4r1q _4jy0 _4jy3 _4jy1 _51sy selected _42ft').click()





