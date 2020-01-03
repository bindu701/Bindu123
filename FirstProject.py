from selenium import webdriver
import time
var111 = input("Enter Input")
var = webdriver.Chrome('C:/Users/bindu.gambhir/Desktop/chromedriver.exe')
time.sleep(8);
var.get(var111);
var.maximize_window();
time.sleep(8);