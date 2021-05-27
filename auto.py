from selenium import webdriver
from time import sleep as wait
path= "F:/chrome/chromedriver.exe"
browser = webdriver.Chrome(path) 

browser.get("https://www.codechef.com")
print(browser.title)
username_element = browser.find_element_by_id("edit-name")
username_element.send_keys("uddeshya")
password_element = browser.find_element_by_id("edit-pass")
from getpass import getpass
password_element.send_keys(getpass("ENTER PASSWORd: "))
wait(5)
browser.find_element_by_id("edit-submit").click()
code_element = browser.find_element_by_id('edit-program')
code_element.send_keys(code)
browser.find_element_by_xpath

