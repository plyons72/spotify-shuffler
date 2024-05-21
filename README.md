# spotify-shuffler
I make no claims as to the safety of this program. I advise anyone who chooses to use it to 
create a copy of their playlist and run the program in that copy. In the event that the program 
crashes mid-run, songs may have been deleted and not added back in. The original playlist can 
then backfill the missing songs to the copy. This is something I intend to work on in the future

Get all entries from spotify playlist(s), delete them, shuffle them, then add them back in, since 
Spotify can't figure out a simple randomizer function. 

Create a spotify app at https://developer.spotify.com/ to generate some API credentials. Set 
client ID and secret appropriately in script. The Redirect URI doesnt matter. Keep it set it to 
localhost if you want, but make sure you set it in the spotify developer site when creating the app 
as well. The important thing to note is that when the script is run, it will open a browser, have 
you sign in, and will redirect you to this site. If you get an error on the webpage, that's fine. 
Just copy the address in the browser and paste it in the terminal where the script is run. 

```
$ python3 spotify-shuffler.py 
Go to the following URL: https://accounts.spotify.com/authorize?client_id=x&response_type=code&redirect_uri=http%3A%2F%2Flocalhost&scope=playlist-modify-private&show_dialog=True
Enter the URL you were redirected to: http://localhost/?code=x
Shuffling songs in playlist: "My Songs"
    Getting list of songs from playlist
    Total tracks in playlist: 333
    Deleting songs from playlist
    Shuffling and adding songs back in
    Songs shuffled and added back to the playlist successfully.

Shuffling songs in playlist: "My other songs"
    Getting list of songs from playlist
    Total tracks in playlist: 622
    Deleting songs from playlist
    Shuffling and adding songs back in
    Songs shuffled and added back to the playlist successfully.
```

The script will run and present you with a url to visit. Click the link, press the accept button, 
and you will be redirected to a new page. This should look like a dead link, but in the search bar 
you will see a URL. Copy the full url and paste it back in the terminal where the script was run. 

If everything works correctly, the playlist will be shuffled, and a cached token will be saved 
locally as `token.txt` so that subsequent runs of the script do not require reauthorization. 

The idea here is to shuffle the playlist, and then play it through without using Spotify's 
shuffle algorithm, since their developers dont know how basic randomization works, and I 
hear the same 50 songs over and over again in a 600 song playlist. 

We are limited by Spotify's Rate Limiting algorithm, and a limit of 100 songs per transaction 
(get, post, delete), so we have to manage slices of songs to work with that does not exceed 
either of these limits

Enjoy. 