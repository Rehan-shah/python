import requests
import json
from datetime import date
from scraper import scrape_instagram_posts
from scraper import scrape_inshort


categories = ["national", "business", "world", "technology"]

# Get today's date
today = date.today().strftime('%Y-%m-%d')

# Load the existing data from the JSON file
with open('news_data.json', 'r') as file:
    news_data = json.load(file)

# Check if the date already exists in the JSON data
if today not in news_data:
    news_data[today] = {}  # Create the date key if it doesn't exist

# Loop through the categories and retrieve one news title per category
for category in categories:
    # Send a GET request to the API
    news_data[today][category] = scrape_inshort(category)

# world ecnomci forum
signa = ''
try:
    arr_wef = scrape_instagram_posts("worldeconomicforum")
except ConnectionError as error:
    signa = f"could not world econocmi forum data: {error}"
else:
    for n in range(len(arr_wef)):
        news_data[today][f"worldeconomic{n + 1}"] = arr_wef[n][f"we{n + 1}"]

# Save the updated news data to the JSON file


with open('news_data.json', 'w') as file:
    json.dump(news_data, file, indent=4)

print('News data added to the JSON file.' + signa)
