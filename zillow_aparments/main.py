from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language":""
}

sf_apparment = requests.get(url="https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22:%7B%7D,%22mapBounds%22:%7B%22north%22:37.861475149802516,%22south%22:37.6660592874218,%22east%22:-122.32679714185346,%22west%22:-122.55682338697065%7D,%22regionSelection%22:%5B%7B%22regionId%22:20330,%22regionType%22:6%7D%5D,%22isMapVisible%22:true,%22filterState%22:%7B%22ah%22:%7B%22value%22:true%7D,%22fr%22:%7B%22value%22:true%7D,%22fsba%22:%7B%22value%22:false%7D,%22fsbo%22:%7B%22value%22:false%7D,%22nc%22:%7B%22value%22:false%7D,%22cmsn%22:%7B%22value%22:false%7D,%22auc%22:%7B%22value%22:false%7D,%22fore%22:%7B%22value%22:false%7D,%22mp%22:%7B%22max%22:3000%7D,%22price%22:%7B%22max%22:587107%7D,%22beds%22:%7B%22min%22:1%7D%7D,%22isListVisible%22:true,%22mapZoom%22:12,%22usersSearchTerm%22:%22San%20Francisco%20CA%22%7D" , headers=header)  

soup = BeautifulSoup(sf_apparment.content, 'html.parser')


prices = soup.find_all(name="span" ,class_='iMKTKr')
address = soup.find_all(name="address")
links = soup.find_all(name="a" , class_="property-card-link")


aparment = []


for i in range(len(prices)):
    aparment.append({
        'price': prices[i].text,
        "address": address[i].text,
        "link":"https://www.zillow.com"+links[i]["href"]
    })


print(aparment)


for n in aparment:
    driver = webdriver.Edge("/Users/Rehan/msedgedriver.exe")
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfsra7jT4OHTtLnfGavjM-ViYhUO_34ci6XB8QG8CtLtUMavg/viewform")
    sleep(2)
    address_in = driver.find_element(By.XPATH , '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_in = driver.find_element(By.XPATH , '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH , '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    address_in.send_keys(n["address"])
    price_in.send_keys(n["price"])
    link.send_keys(n["link"])


    button = driver.find_element(By.XPATH ,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    button.click()

    driver.quit()

