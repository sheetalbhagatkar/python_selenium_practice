from selenium import webdriver
#from selenium.webdriver.common.keys import keys

browser=webdriver.Chrome()
browser.get("http://selenium.dev/")

browser.maximize_window()
title=browser.title
print(title)
#check title
assert "Selenium" in title
