from selenium import webdriver


# driver=webdriver.Ie()
# driver=webdriver.Firefox()
#create object
browser=webdriver.Chrome()
browser.get("https://www.gmail.com/")
print(browser.title)
print(browser.current_url)
#print(driver.page_source)
(browser.close())

