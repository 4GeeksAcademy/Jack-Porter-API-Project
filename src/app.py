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
client_secret = os.environ.get("CLIENT_SECRET")

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(auth_manager=auth_manager)

artist_id = "6DPYiyq5kWVQS4RGwxzPC7"
artist_best_tracks = spotify.artist_top_tracks(artist_id)

top_songs = []
for track in artist_best_tracks[track]:
    top_songs.append ({
        'name': track[]
    })