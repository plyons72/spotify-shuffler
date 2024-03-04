import os
import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set your Spotify API credentials
# https://developer.spotify.com/
CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = "http://localhost"

# Set your spotify playlist ID. If you open spotify, click on the playlist, 
# and create a link to it, the ID will be where the Xs are below
# https://open.spotify.com/playlist/XXXXXXXXXXXXXXXXXXXXXX?si=YYYYYYYYYYYYYYYYY
PLAYLIST_ID = ""

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    ))

# Function to get all songs from the playlist
def get_playlist_songs(playlist_id):
    print("Getting playlist songs")
    results = sp.playlist_items(playlist_id)
    songs = [item['track']['id'] for item in results['items']]
    return songs

# Function to delete all songs from the playlist
def delete_playlist_songs(playlist_id, songs):
    sp.playlist_remove_all_occurrences_of_items(playlist_id, songs)

# Function to add songs to the playlist in a shuffled order
def add_songs_shuffled(playlist_id, song_ids):
    random.shuffle(song_ids)
    sp.playlist_add_items(playlist_id, song_ids)

# Get all songs from the playlist
print("Getting list of songs from playlist")
playlist_songs = get_playlist_songs(PLAYLIST_ID)

# Delete all songs from the playlist
print("Deleting songs from playlist")
delete_playlist_songs(PLAYLIST_ID, playlist_songs)

# Add the songs back to the playlist in a shuffled order
print("Shuffling and adding songs back in")
add_songs_shuffled(PLAYLIST_ID, playlist_songs)

print("Songs shuffled and added back to the playlist successfully.")