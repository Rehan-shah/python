from collections.abc import ByteString
import os
from time import sleep 
import dotenv 
from util import SpeedData
from selenium import webdriver
from selenium.webdriver.common.by import By

dotenv.load_dotenv()
class TwittManger():

    def __init__(self) -> None:
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.driver = webdriver.Edge() 

    def tweet_complain(self):
        pass

    def authenticate(self):
        self.driver.get("https://twitter.com/")
        sleep(10)
        email_input = self.driver.find_element(By.XPATH , '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email_input.send_keys(self.email)
        next_btn = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_btn.click()
        sleep(10)
        user_input = self.driver.find_element(By.XPATH , '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        user_input.send_keys(os.getenv("USERNAME"))
        btn = self.driver.find_element(By.XPATH , '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
        btn.click()
        sleep(10)

        password_input = self.driver.find_element(By.XPATH , '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input') 
        password_input.send_keys(self.password)

        login_btn = self.driver.find_element(By.XPATH , '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login_btn.click()
        sleep(100)

    def send_tweet(self , speed : SpeedData):
        self.driver.get("https://twitter.com/")
        sleep(10)
        email_input = self.driver.find_element(By.XPATH , '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email_input.send_keys(self.email)
        next_btn = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_btn.click()
        sleep(10)
        user_input = self.driver.find_element(By.XPATH , '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        user_input.send_keys(os.getenv("USERNAME"))
        btn = self.driver.find_element(By.XPATH , '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
        btn.click()
        sleep(10)

        password_input = self.driver.find_element(By.XPATH , '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input') 
        password_input.send_keys(self.password)

        login_btn = self.driver.find_element(By.XPATH , '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        login_btn.click()
        # sleep(30)
        input("o0f3 0f03i")
        input_T = self.driver.find_element(By.CSS_SELECTOR ,'div[contenteditable]')

        input_T.send_keys(f"Hey , I paid {speed.promised_down}/{speed.promised_up} but getting {speed.actuall_down}/{speed.actuall_up}")

        send_tweet = self.driver.find_element(By.XPATH , '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div')
        send_tweet.click()
        input("o0r")


        self.driver.quit()
        


