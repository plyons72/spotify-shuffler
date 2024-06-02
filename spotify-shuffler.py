import random
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set your Spotify API credentials
# https://developer.spotify.com/
CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = "http://localhost"

# Set your spotify playlist ID(s). If you open spotify, click on the playlist, 
# and create a link to it, the ID will be where the Xs are below
# https://open.spotify.com/playlist/XXXXXXXXXXXXXXXXXXXXXX?si=YYYYYYYYYYYYYYYYY
# Program can operate on a single playlist or multiple if list is provided
PLAYLIST_IDS = ["", ""]

# Instantiate spotipy client
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-modify-private",
        show_dialog=True,
        open_browser=False,
    )
)

# Function to get all songs from the playlist
def get_playlist_songs(playlist_id):
    # Get total number of tracks so we can loop over all of them. API only allows 100 at a time
    num_tracks = sp.playlist_items(playlist_id, fields='total')['total']
    songs = []
    index = 0
    while index < num_tracks:
        # Call returns dict of items:track:id. Just get a list of IDs to operate on
        results = (sp.playlist_items(playlist_id, limit=100, fields='items.track.id', offset=index))
        for item in results['items']:
            songs.append(item['track']['id'])
        index = index + 100
    # Delete duplicate songs
    songs = list(set(songs))
    return songs, len(songs)

# Function to delete all songs from the playlist
def delete_playlist_songs(playlist_id, songs, num_tracks):
    # Helpers to keep track of our slices
    first = 0
    last = 100
    # If we have more than 100 songs, loop through until we've deleted all songs in chunks of 100
    if num_tracks > 100:
        while first < num_tracks:
            sp.playlist_remove_all_occurrences_of_items(playlist_id, songs[first:last])
            first = first + 100
            last = last + 100 if last + 100 < num_tracks else num_tracks
    else:
        sp.playlist_remove_all_occurrences_of_items(playlist_id, songs)


# Function to add songs to the playlist in a shuffled order
def add_songs_shuffled(playlist_id, songs, num_tracks):
    # Helpers to keep track of our slices
    first = 0
    last = 100
    # Randomize the list
    random.shuffle(songs)
    # If we have more than 100 songs, loop through until we've added all songs in chunks of 100
    if num_tracks > 100:
        while first < num_tracks:
            sp.playlist_add_items(playlist_id, songs[first:last])
            first = first + 100
            last = last + 100 if last + 100 < num_tracks else num_tracks
    else:
        sp.playlist_add_items(playlist_id, songs)

def main():
    # Loop over list of playlists
    for playlist_id in PLAYLIST_IDS:
        name = sp.playlist(playlist_id, fields="name")
        print("\nShuffling songs in playlist: \"{}\"".format(name['name']))

        # Get all songs from the playlist
        print("\tGetting list of songs from playlist")
        playlist_songs, num_tracks = get_playlist_songs(playlist_id)
        print("\tTotal tracks in playlist: {}".format(num_tracks))


        # Delete all songs from the playlist
        print("\tDeleting songs from playlist")
        delete_playlist_songs(playlist_id, playlist_songs, num_tracks)

        # Add the songs back to the playlist in a shuffled order
        print("\tShuffling and adding songs back in")
        add_songs_shuffled(playlist_id, playlist_songs, num_tracks)

        print("\tSongs shuffled and added back to the playlist successfully.")

if __name__ == "__main__":
    main()