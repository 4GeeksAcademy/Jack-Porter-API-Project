import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# load the .env file variables
CLIENT_ID= "62da616b1a484fde9deecc041b33429f"
CLIENT_SECRET="DS12_API_Secret"

load_dotenv()


# Spotify API credentials
client_id = os.environ.get("CLIENT_ID")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
spotify = spotipy.Spotify(auth_manager=auth_manager)

artist_id = "6DPYiyq5kWVQS4RGwxzPC7"

# Getting the top 3 most popular songs
results = spotify.artist_top_tracks(artist_id)["tracks"]
top_songs = []
for track in results:
    top_songs.append({
        'name': t['name'],
        'duration_min': t['duration_ms']['name'],
        'popularity': t['popularity'],
        'preview_url': t['preview_url'],})

track_df = pd.dataframe(top_songs)

print(track_df(3))

plt.scatter(track_df['duration_min'], track_df['popularity'])
plt.xlabel('Duration (Min)')
plt.ylabel('Popularity')
plt.title('Comparison of Popularity and Song Length')
plt.show()