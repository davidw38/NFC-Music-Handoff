import os

path = os.path.realpath(__file__)

if (os.path.exists(path[:-6] + "airplay.txt")):
    os.remove(path[:-6] + "airplay.txt")

if (os.path.exists(path[:-6] + "airplay2txt")):
    os.remove(path[:-6] + "airplay2.txt")
    
