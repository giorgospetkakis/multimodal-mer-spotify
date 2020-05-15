import subprocess
from collections import namedtuple
import json
import csv
import re
from difflib import SequenceMatcher

class Track:
    def __init__(self, artists, name):
        self.artists, self.name = artists, name

class Artists:
    def __init__(self, artists):
        self.artists = [a.name for a in artists]

def customDecoder(artistDict):
    return namedtuple('X', artistDict.keys())(*artistDict.values())

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Some API stuff
URL_ID = "https://api.spotify.com/v1/search?q="
URL_FEATURES = "https://api.spotify.com/v1/audio-features/"
URL_TRACK = "https://api.spotify.com/v1/tracks/"

command = 'curl -sS -X "GET"'
PARAM = "&type=track&limit=1&offset=0"
ACC = "Accept: application/json"
TYP = "Content-Type: application/json"
AUTH = "Authorization: Bearer " ## ENTER AUTH KEY ##

# Extract the tracks from the csv file
entries = []
with open('MoodyLyrics4Q/MoodyLyrics4Q.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        entries += [row]
    f.close()
clean_entries = [re.sub(r"[^a-zA-Z0-9 ]+", '', x).lower() for e in entries[1:] for x in e[1:]]
pairs = []
for i in range(0,len(clean_entries),3):
    pairs += [[clean_entries[i], clean_entries[i+1], clean_entries[i+2]]]

# Generate API query strings to fetch song ids
queries = [re.sub(r" ", "%20", c[0]) + "%20" + re.sub(r"\s", "%20", c[1]) for c in pairs]

# Run Queries
features = []
idx = []
found = 0 ; not_found = 0
for i, q in enumerate(queries):
    db_artist = pairs[i][0]
    db_song_name = pairs[i][1]

    # Get song ids
    res = subprocess.check_output(f'{command} "{URL_ID}{q}{PARAM}" -H "{ACC}" -H "{TYP}" -H "{AUTH}"', shell=True)
    # Get all song id's in the search
    filtered = re.search(r"https:\/\/api\.spotify\.com\/v1\/tracks\/(.*?)\"", str(res))
    if (filtered == None):
        continue

    track_id = ""
    _id = filtered.group(1)
    # Iterate through all found song ids
    # Get information on the ids
    validate = subprocess.check_output(f'{command} "{URL_TRACK}{str(_id)}" -H "{ACC}" -H "{TYP}" -H "{AUTH}"', shell=True)
    # Deserialize information from JSON
    response = json.loads(validate, object_hook=customDecoder)
    song_name = response.name ; artist_names = [a.name for a in response.artists]

    ## Filter everything out that may introduce noise
    song_name = re.sub(r"[^a-zA-Z0-9 ]+", '', song_name).lower()
    artist_names = [re.sub(r"[^a-zA-Z0-9 ]+", '', a).lower() for a in artist_names]

    max_similarity = 0
    max_artist = ""
    for artist in artist_names:
        sim = similar(artist, db_artist)
        if sim > max_similarity:
            max_similarity = sim
            max_artist = artist

    similarity = similar(song_name, db_song_name) + max_similarity
    if (similarity >= 1.5):
        if (similarity < 2.0):
            track_id = _id
            found += 1

    if (track_id==""):
        continue

    # Get song features
    feat = subprocess.check_output(f'{command} "{URL_FEATURES}{track_id}" -H "{ACC}" -H "{TYP}" -H "{AUTH}"', shell=True)
    # Deserialize from JSON
    serialized = json.loads(feat, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    features += [serialized]
    idx += [i]

print(f"Songs found: {found}")

# Get rid of 404s
features = [f for f in features if len(list(f)) > 1]

# Write all to csv 
# Re-ordering the dataset to prioritize musical terms and meta-data
header_line = "id,artist,title,mood,duration_ms,key,tempo,time_signature,danceability,energy,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence\n"
append = open("SpotifyData-1.csv", "a")
append.writelines(header_line)

# Need to cross-reference the song indices that were compatible with the Spotify data
for j, f in enumerate(features):
    string = str(f.id) + "," + pairs[j][0] + "," + pairs[j][1] + "," + pairs[j][2] + "," + str(f.duration_ms) + "," + str(f.key) + "," + str(f.tempo) + "," + str(f.time_signature) + "," + str(f.danceability) + "," + str(f.energy)  + "," + str(f.loudness) + "," + str(f.mode) + "," + str(f.speechiness) + "," + str(f.acousticness) + "," + str(f.instrumentalness) + "," + str(f.liveness) + "," + str(f.valence) + "\n"
    append.writelines(string)
append.close()