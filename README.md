# spotify-shuffler
Get all entries from spotify playlist, delete them, shuffle them, then add them back in, since 
Spotify can't figure out a simple randomizer function. 

Create a spotify app at https://developer.spotify.com/ to generate some API credentials. Set 
client ID and secret appropriately in script. The Redirect URI doesnt matter. Set it to localhost 
if you want, but make sure you set it in the spotify developer site when creating the App as well... 
The important thing to note is that when the script is run, it will open a browser, have you sign in, 
and will redirect you to this site. If you get an error on the webpage, that's fine. Just copy the 
address in the browser and paste it in the terminal where the script is run. 

```
$ python3 spotify-shuffler.py 
Getting list of songs from playlist
Getting playlist songs
Enter the URL you were redirected to: http://localhost/?code=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Deleting songs from playlist
Shuffling and adding songs back in
Songs shuffled and added back to the playlist successfully.
```

Note the `Enter the URL you were redirected to:` line. It just needs to extract a code from the 
redirect url so that it can proceed with client auth and perform the shuffling. 