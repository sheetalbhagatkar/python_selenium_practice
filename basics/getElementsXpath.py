from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Edge()
driver.get("http://www.google.com")
driver.maximize_window()
print(driver.title)
search_text=driver.find_element(By.XPATH,"#APjFqb")
# driver.find_element(by=xpa)