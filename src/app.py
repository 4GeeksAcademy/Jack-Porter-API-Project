import os
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv

# load the .env file variables
CLIENT_ID= "62da616b1a484fde9deecc041b33429f"
CLIENT_SECRET="e7925298fa5a46ed82266cc7255cc519"

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
        'name': track['name'],
        'duration_min': track['duration_ms']/60000,
        'popularity': track['popularity'],
        'external_urls': track['external_urls'],})

track_df = pd.DataFrame(top_songs)

print(track_df.head(3))

plt.scatter(track_df['duration_min'], track_df['popularity'])
plt.xlabel('Duration (Min)')
plt.ylabel('Popularity')
plt.title('Comparison of Popularity and Song Length')
plt.savefig("Durationplt.jpg")