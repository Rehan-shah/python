
from selenium import webdriver
from selenium.webdriver.common.by import By

edge_driver_path = "/Users/Rehan/msedgedriver"

driver = webdriver.Edge(executable_path=edge_driver_path)


driver.get("http://secure-retreat-92358.herokuapp.com")

f_name_input = driver.find_element(By.NAME , "fName")
f_name_input.send_keys("Rehan")

l_name_input = driver.find_element(By.NAME , "lName")
l_name_input.send_keys("Shah")

email_input = driver.find_element(By.NAME , "email")
email_input.send_keys('Rehansnehalshah1@gmail.com')

btn = driver.find_element(By.CLASS_NAME,"btn")
btn.click()


input("Did you finsh seeing the message?")

driver.quit()


