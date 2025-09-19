from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Edge()
url="https://www.saucedemo.com/"
user_name="standard_user"
password="secret_sauce"
driver.get(url)
driver.maximize_window()
print(driver.title)

#locate Values
username_field=driver.find_element(By.ID,'user-name')
password_field=driver.find_element(By.ID,'password')

#set user and password
username_field.send_keys(user_name)
password_field.send_keys(password)

#get button xpath and assert if button not disabled
login_button=driver.find_element(By.ID,'login-button')
assert not login_button.get_attribute("disabled")

#click login
login_button.click()

#check if able to logged in
success_element=driver.find_element(By.CSS_SELECTOR,'.title')
assert success_element.text=="Products"