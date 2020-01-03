from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome('C:/Users/bindu.gambhir/Desktop/chromedriver.exe')

driver.get('https://www.w3.org/')
time.sleep(3)
driver.quit()