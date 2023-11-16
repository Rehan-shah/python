from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class InterentSpeed():

    def __init__(self , up_speed ,down_speed) -> None:
        self.up_speed = up_speed
        self.down_speed = down_speed
        self.driver = webdriver.Edge()
    

    def get_speed(self) -> (float , float):
        """
         1st paramater is the down speed
         2nd paramater is the up speed
        """ 
        self.driver.get("https://www.speedtest.net/") 

        button = self.driver.find_element(By.XPATH , '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')

        button.click()
        input("heuuu u done")
        # time.sleep(2*60)

        down_speed = self.driver.find_element(By.XPATH , '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')

        up_speed = self.driver.find_element(By.XPATH , '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')

        self.driver.quit()
                                              

        return (float(down_speed.text), float(up_speed.text))
        
    def is_speed_lower(self, up_speed:float , down_speed:float) -> bool:
        if  self.down_speed > down_speed:
            return False
        if self.up_speed > up_speed:
            return False

        return True


