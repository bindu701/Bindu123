from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://www.w3.org/')
for a in driver.find_elements_by_xpath('.//a'):
    print(a.get_attribute('href'))