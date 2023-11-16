import json
from datetime import datetime
from bs4 import BeautifulSoup
import requests
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
 
# Create a Spotify API Client
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
        cache_path="token.txt",
        redirect_uri=os.environ.get("SPOTIPY_REDIRECT_URI"),
        scope="playlist-modify-private",
        username="Rehan Shah",  # email might also work, I haven't tested it
    )
)

user_id = sp.current_user()["id"]


date = input("Which date would you like search for yyyyy-mm-dd :")


year = date.split("-")[0]

list_url = []


contents = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")


soup = BeautifulSoup(contents.text ,"html.parser")

heading = soup.select(selector=".c-title.a-no-trucate.a-font-primary-bold-s")

for song in heading:
    query = f"track:{song.text.strip()} year:{year}"
    results = sp.search(q=song.text.strip(), type="track", limit=1)
    try :
        list_url.append(results["tracks"]["items"][0]["uri"])
    except KeyError:
        print("No song found")

print(list_url)
    

playlist = sp.user_playlist_create(user=user_id, name=f"Billboard 100", public=False, description="")
                        
sp.playlist_add_items(playlist["id"],items=list_url)




# try :
#     (year, month, day) = date.split("-")
# except :
#     raise ValueError("Invalid date format")
#
# date = datetime(year=int(year) , month=int(month), day=int(day) )
# date_now = datetime.now()
#
# if date_now > date:
#     raise ValueError("Invalid date , date must older than current date")
#


