import spotipy.util
import os

path = os.path.realpath(__file__)

idformat = "ClientID:"
secretformat = "ClientSecret:"
usernameformat = "Username:"

memoryline = "";

scopes = "user-read-currently-playing user-modify-playback-state user-read-playback-state streaming app-remote-control"
url = "http://localhost/"

with open('config.txt', 'r') as file:
    for line in file:
        if idformat in line:
            memoryline = line
            id = memoryline.rstrip(os.linesep)[11:][:-1]
        elif secretformat in line:
            memoryline = line
            secret = memoryline.rstrip(os.linesep)[15:][:-1]
        elif usernameformat in line:
            memoryline = line
            username = memoryline.rstrip(os.linesep)[11:][:-1]

token = spotipy.util.prompt_for_user_token(username, scopes, id, secret, url)

spotify = spotipy.Spotify(auth=token)

print(spotify.devices())