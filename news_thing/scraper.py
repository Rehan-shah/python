import requests
from bs4 import BeautifulSoup
from requests.api import options
from selenium import webdriver
import time


def scrape_instagram_posts(username):
    url = f"https://www.instagram.com/{username}/"

    chrome_options = webdriver.EdgeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Edge()
    driver.get(url)
    time.sleep(10)
    response = driver.page_source
    soup = BeautifulSoup(response, "html.parser")
    post_links = soup.findAll("img", attrs={"class": "xu96u03"})
    post_links = post_links[len(post_links)-2:]
    dic = []
    i = 1
    for img in post_links:
        print(img["alt"])
        text = img["alt"]
        text = text.replace("\n", " ")
        if "Learn more" in text:
            text = text[:text.index("Learn more")]
        if "Submit" in text:
            text = text[:text.index("Submit")]
        if "Click" in text:
            text = text[:text.index("Click")]
        dic.append({f"we{i}": text})
        i += 1
        print(text)
    driver.quit()
    return dic


def scrape_inshort(category):
    url = f"https://www.inshorts.com/en/read/{category}/"

    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-gpu")
    # driver = webdriver.Chrome(options=chrome_options)
    #
    driver = webdriver.Edge()
    driver.get(url)
    time.sleep(5)  # any number > 3 should work fine
    response = driver.page_source
    soup = BeautifulSoup(response, "html.parser")
    post_links = soup.findAll("span", attrs={"itemprop": "headline"})
    post_links = post_links[:1]

    driver.quit()
    return  post_links[0].get_text()

