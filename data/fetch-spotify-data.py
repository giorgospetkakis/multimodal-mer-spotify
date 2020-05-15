import subprocess
from collections import namedtuple
import json
import csv
import re

# Some API stuff
URL_ID = "https://api.spotify.com/v1/search?q="
URL_FEATURES = "https://api.spotify.com/v1/audio-features/"

PARAM = "&type=track&limit=10&offset=5"
ACC = "Accept: application/json"
TYP = "Content-Type: application/json"
AUTH = "Authorization: Bearer KEY" ## ENTER AUTH KEY ##


# Extract the tracks from the csv file
entries = []
with open('MoodyLyrics4Q/MoodyLyrics4Q.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        entries += [row]
    f.close()

# Generate API Queries to fetch song ids
queries = [re.sub(r" ", "%20", e[1]) + "%20"+ re.sub(r"\s", "%20", e[2]) for e in entries[1:]]

# Run Queries
features = []
idx = []
for i, q in enumerate(queries):
    # Get song ids
    res = subprocess.check_output(f"curl -X \"GET\" \"{URL_ID}{q}{PARAM}\" -H \"{ACC}\" -H \"{TYP}\" -H \"{AUTH}\"", shell=True)
    filtered = re.search(r"https:\/\/api\.spotify\.com\/v1\/tracks\/(.*?)\"", str(res))
    if (filtered == None):
        continue
    # Get song features
    feat = subprocess.check_output(f'curl -X "GET" "{URL_FEATURES}{filtered.group(1)}" -H "{ACC}" -H "{TYP}" -H "{AUTH}"', shell=True)
    serialized = json.loads(feat, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    features += [serialized]
    idx += [i]

header_line = "id,artist,title,mood,duration_ms,key,tempo,time_signature,danceability,energy,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence\n"
append = open("SpotifyData-1.csv", "a")
append.writelines(header_line)
for j, f in enumerate(features):
    string = str(f.id) + "," + entries[idx[j]+1][1] + "," + entries[idx[j]+1][2] + "," + entries[idx[j]+1][3] + "," + str(f.duration_ms) + "," + str(f.key) + "," + str(f.tempo) + "," + str(f.time_signature) + "," + str(f.danceability) + "," + str(f.energy)  + "," + str(f.loudness) + "," + str(f.mode) + "," + str(f.speechiness) + "," + str(f.acousticness) + "," + str(f.instrumentalness) + "," + str(f.liveness) + "," + str(f.valence) + "\n"
    append.writelines(string)
append.close()