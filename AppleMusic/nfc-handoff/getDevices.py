import spotipy.util
import os

path = os.path.realpath(__file__)

idformat = "ClientID:"
idline = ""

secretformat = "ClientSecret:"
secretline = ""

usernameformat = "Username:"
usernameline = ""

scopes = "user-read-currently-playing user-modify-playback-state user-read-playback-state streaming app-remote-control"
url = "http://localhost/"

with open('config.txt', 'r') as file:
    for line in file:
        if idformat in line:
                idline = line
                id = idline[11:][:-2]
        elif secretformat in line:
                secretline = line
                secret = secretline[15:][:-2]
        elif usernameformat in line:
                usernameline = line
                username = usernameline[11:][:-1]

token = spotipy.util.prompt_for_user_token(username, scopes, id, secret, url)

spotify = spotipy.Spotify(auth=token)

print(spotify.devices())