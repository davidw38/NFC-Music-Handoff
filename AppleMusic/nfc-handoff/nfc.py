import spotipy.util
import os

if os.path.exists("dry-run"):

    idformat = "ClientID:"
    idline = ""

    secretformat = "ClientSecret:"
    secretline = ""

    usernameformat = "Username:"
    usernameline = ""

    deviceformat = "Device:"
    deviceline = ""

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
            elif deviceformat in line:
                    deviceline = line
                    device = deviceline[9:][:-1]

    token = spotipy.util.prompt_for_user_token(username, scopes, id, secret, url)

    spotify = spotipy.Spotify(auth=token)

    songlist = spotify.search("test", 1, 0, "track", "DE")

else:
    path = os.path.realpath(__file__)
    os.remove(path[:-6] + "log.txt")

    timecodeformat = '"ssnc" "prgr":'
    timecodeline = ""

    songnameformat = "Title:"
    songnameline = ""

    idformat = "ClientID:"
    idline = ""

    secretformat = "ClientSecret:"
    secretline = ""

    usernameformat = "Username:"
    usernameline = ""

    deviceformat = "Device:"
    deviceline = ""

    countryformat = "Country:"
    countryline = ""

    scopes = "user-read-currently-playing user-modify-playback-state user-read-playback-state streaming app-remote-control"
    url = "http://localhost/"

    i = 3
    q = 3

    with open(path[:-6] + 'config.txt', 'r') as file:
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
            elif deviceformat in line:
                    deviceline = line
                    device = deviceline[9:][:-2]
            elif countryformat in line:
                    countryline = line
                    country = countryline[10:][:-2]

    with open(path[:-6] + 'airplay.txt', 'r') as file:
        for line in file:
            if timecodeformat in line:
                if i > 1:
                    i = i-1
                else:
                    timecodeline = line
                    break

    with open(path[:-6] + 'airplay2.txt', 'w') as file:
        file.write(timecodeline)

    with open(path[:-6] + 'airplay.txt', 'r') as file:
        for line in file:
            if songnameformat in line:
                    songnameline = line
                    songname = songnameline[8:][:-3]
                    break

    timecodeline2 = timecodeline[16:]
    timecodeline3 = timecodeline2[:-3]

    timecodes = timecodeline3.split("/")
    starter = int(timecodes[0])
    mid = int(timecodes[1])
    end = int(timecodes[2])

    curr = round((mid - starter) / 44100)
    dur = round((end - starter) / 44100)

    token = spotipy.util.prompt_for_user_token(username, scopes, id, secret, url)

    spotify = spotipy.Spotify(auth=token)

    songlist = spotify.search(songname, 1, 0, "track", country)
    song = songlist['tracks']['items'][0]['uri']

    spotify.start_playback(device, None, [song], None)
    spotify.seek_track(int(curr) * 1000, device)

    with open(path[:-6] + 'log.txt', 'w') as file:
        file.write("Songname: " + songname + "\n"
                +  "Timecode 1: " + str(starter) + "\n"
                +  "Timecode 2: " + str(mid) + "\n"
                +  "Timecode 3: " + str(end) + "\n"
                +  "Timecode: " + timecodeline2 + "\n"
                +  "Curr: " + str(curr) + "\n"
                +  "Dur: " + str(dur))

    os.remove(path[:-6] + "airplay.txt")
    os.remove(path[:-6] + "airplay2.txt")