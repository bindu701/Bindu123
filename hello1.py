import selenium
# Using Chrome to access web
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/bindu.gambhir/Desktop/chromedriver.exe')
# Open the website
driver.get('https://canvas.case.edu')

