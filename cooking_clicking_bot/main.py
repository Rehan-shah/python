from logging import warn
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


edge_path = "Users/Rehan/msedgedriver"
driver = webdriver.Edge(executable_path=edge_path)


driver.get("https://orteil.dashnet.org/experiments/cookie/")


t_end = time.time() + 60 * 5
t_5 = time.time() + 5

def click_upgrade():
    print("5 secs")
    for i in range(len(updgrade_list)-1 , -1, -1):
        try :
            if updgrade_list[i].is_displayed(): 
                updgrade_list[i].click()
        except:
            pass


while time.time() < t_end:
    cookie = driver.find_element(By.ID,"cookie")
    cookie.click()
    
    updgrade_list = driver.find_elements(By.CSS_SELECTOR,"#store div")
    if time.time() > t_5:
        click_upgrade()
        t_5 = time.time() +5
    
    

print(driver.find_element(By.ID , "money").text)


input("Did finsh viweing ?")


driver.quit()
