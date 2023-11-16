from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

driver = webdriver.Edge()


driver.get("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")


json = []

def add_json(): 
    global json
    rows = driver.find_elements(By.CLASS_NAME , "data-table__row")


    for col in rows :
        format = col.text
        array = format.split("\n")
        array[2] = array[2].replace("$" , "").replace("%","").replace(",","").split(" ")
        try:
            arr = int(array[2][3])/100
        except:
            arr = " "
        json.append({
            "Major": array[1],
            "Degree Type": array[2][0],
            "Early Career Pay": int(array[2][1]),
            "Mid-Career Pay": int(array[2][2]),
            "High Meaning": arr
        })
  
add_json()

click =  driver.find_element(By.XPATH , '//*[@id="__next"]/div/div[1]/article/div[3]/a[3]')

click.click()

add_json()


df = pd.DataFrame(json)

df.to_csv("data.csv")
