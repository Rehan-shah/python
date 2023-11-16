from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Edge()


driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")


sign_in = driver.find_element(By.XPATH , "/html/body/div[1]/header/nav/div/a[2]")


sign_in.click()


sleep(2)


email_input = driver.find_element(By.XPATH , '//*[@id="username"]')
password_input = driver.find_element(By.XPATH , '//*[@id="password"]')
sign_in_btn = driver.find_element(By.XPATH , '//*[@id="organic-div"]/form/div[3]/button')

email_input.send_keys("Rehansnehalshah1@gmail.com")
password_input.send_keys('Rehan1234')
sign_in_btn.click()


sleep(5)


input("you done")


driver.quit()
