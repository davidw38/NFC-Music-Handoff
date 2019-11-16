import spotipy.util
import os
import traceback

if os.path.exists("dry-run"):

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

    songlist = spotify.search("test", 1, 0, "track", "DE")

else:

    idformat = "ClientID:"
    secretformat = "ClientSecret:"
    usernameformat = "Username:"
    countryformat = "Country:"
    deviceformat = "Device:"

    memoryline = "";
    path = os.path.realpath(__file__)

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
            elif countryformat in line:
                memoryline = line
                country = memoryline.rstrip(os.linesep)[10:][:-1]
            elif deviceformat in line:
                memoryline = line
                device = memoryline.rstrip(os.linesep)[9:][:-1]

    try:
        token = spotipy.util.prompt_for_user_token(username, scopes, id, secret, url)
        spotify = spotipy.Spotify(auth=token)
        spotify.transfer_playback(device, True)
    except:
        exe = traceback.format_exc()
        with open(path[:-6] + 'error.txt', 'w') as file:
            file.write(exe)
        raise Exception("The was a problem with the Spotify-API! Check error.txt!")