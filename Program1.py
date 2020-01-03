from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver.support.select import Select

import time

var: WebDriver = webdriver.Chrome("C:/Users/bindu.gambhir/Desktop/chromedriver.exe")


var.get("https://apps.facebook.com/")
var.maximize_window()
# var.find_element_by_xpath("//input[@id='email']").send_keys("bindu.gambhir@yahoo.co.in")
# var.find_element_by_xpath("//input[@id='pass']").send_keys("Hello@09876")
# var.find_element_by_xpath("//input[@id='u_0_m']").send_keys("bindu")
# var.find_element_by_xpath("//input[@id='u_0_o']").send_keys("bindu")
# var.find_element_by_xpath("//input[@id='u_0_r']").send_keys("bindu")
# var.find_element_by_xpath("//input[@id='u_0_w']").send_keys("bindu")
# #var.find_element_by_xpath("//tbody//tr[2]//td[3]//label").click()
# va = Select(var.find_element_by_xpath("//select[@id='day']"))
# va.select_by_value("15")
# va = Select(var.find_element_by_xpath("//select[@id='year']"))
# va.select_by_value("1990")
# va = Select(var.find_element_by_xpath("//select[@id='month']"))
# va.select_by_value("8")
va = var.find_element_by_xpath("//label[contains(text(),'Male')]//preceding-sibling::input")
va.click()
//label[contains(text(),'Fem')]//ancestor::span[1]
//label[contains(text(),'Fem')]//..
//label[contains(text(),'Female')]//preceding-sibling::input//following-sibling::label
//label[contains(text(),'Female')]//preceding::input[1]
//label[contains(text(),'Female')]//preceding::input[@name='sex']