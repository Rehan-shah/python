from time import sleep
from selenium import webdriver
import atexit

from selenium.webdriver.common.by import By

class Instagram():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Edge("/Users/Rehan/msedgedriver.exe")

        def close_driver():
            pass
        atexit.register(close_driver)
        self.driver.get("https://www.instagram.com/")
        sleep(10)
        self.auth()
        self.driver.quit()


    def auth(self):
        email = self.driver.find_element(By.XPATH , '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = self.driver.find_element(By.XPATH , '//*[@id="loginForm"]/div/div[2]/div/label/input')
        login_btn = self.driver.find_element(By.XPATH , '//*[@id="loginForm"]/div/div[3]/button')


        email.send_keys(self.username)
        password.send_keys(self.password)
        login_btn.click()
        input("hi")


insta  = Instagram("h5navcca9o@exelica.com" , "5HY9YwIBce4G")
