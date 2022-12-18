import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
#
# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)


response = requests.get("https://www.billboard.com/charts/hot-100/1995-06-17")
music_page = response.text

soup = BeautifulSoup(music_page, "html.parser")
music_list = soup.select(selector='li #title-of-a-story')
music_titles = [_.getText().strip() for _ in music_list]


YOUR_APP_CLIENT_ID = PLACEHOLDER
YOUR_APP_CLIENT_SECRET = PLACEHOLDER

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=YOUR_APP_CLIENT_ID,
        client_secret= YOUR_APP_CLIENT_ID,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in music_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)