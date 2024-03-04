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
    # Get total number of tracks so we can loop over all of them. API only allows 100 at a time
    total_tracks = sp.playlist_items(playlist_id, fields='total')['total']
    print("Total tracks in playlist: {}".format(total_tracks))
    songs = []
    index = 0
    while index < total_tracks - 1:
        # Call returns dict of items:track:id. Just get a list of IDs to operate on
        results = (sp.playlist_items(playlist_id, fields='items.track.id', offset=index))
        for item in results['items']:
            songs.append(item['track']['id'])
        index = index + 100
    # Make song list a set to remove duplicates
    print("Removing duplicate songs...")
    songs = list(set(songs))
    return songs, len(songs)

# Function to delete all songs from the playlist
def delete_playlist_songs(playlist_id, songs, total_tracks):
    first = 0
    last = 100
    # If we have more than 100 songs, loop through until we've deleted all songs in chunks of 100
    if total_tracks > 100:
        while first < total_tracks:
            sp.playlist_remove_all_occurrences_of_items(playlist_id, songs[first:last])
            first = first + 100
            last = last + 100 if last + 100 < total_tracks else total_tracks
    else:
        sp.playlist_remove_all_occurrences_of_items(playlist_id, songs)

# Function to add songs to the playlist in a shuffled order
def add_songs_shuffled(playlist_id, songs, total_tracks):
    # Helpers to keep track of our slices
    first = 0
    last = 100
    # Randomize the list
    random.shuffle(songs)
    # If we have more than 100 songs, loop through until we've added all songs in chunks of 100
    if total_tracks > 100:
        while first < total_tracks:
            sp.playlist_add_items(playlist_id, songs[first:last])
            first = first + 100
            last = last + 100 if last + 100 < total_tracks else total_tracks
    else:
        sp.playlist_add_items(playlist_id, songs)

def main():
    # Get all songs from the playlist
    print("Getting list of songs from playlist")
    playlist_songs,total_tracks = get_playlist_songs(PLAYLIST_ID)

    # Delete all songs from the playlist
    print("Deleting songs from playlist")
    delete_playlist_songs(PLAYLIST_ID, playlist_songs, total_tracks)

    # Add the songs back to the playlist in a shuffled order
    print("Shuffling and adding songs back in")
    add_songs_shuffled(PLAYLIST_ID, playlist_songs, total_tracks)

    print("Songs shuffled and added back to the playlist successfully.")

if __name__ == "__main__":
    main()