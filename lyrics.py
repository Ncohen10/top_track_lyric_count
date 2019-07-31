import urllib.request
import json
import re
from collections import Counter


API_KEY = "PUT API KEY HERE"

def get_lyric_data(country_code):

    # Gets track ID from the top charts of a country
    # Determined by the country code
    def get_track_id():
        url = ("https://api.musixmatch.com/ws/1.1/chart.tracks.get?apikey="
               + API_KEY + "&chart_name=top&page=1&page_size=5&country="
               + country_code + "&f_has_lyrics=1")
        response = urllib.request.urlopen(url)
        content = response.read().decode()
        content = json.loads(content)
        track_id = content["message"]["body"]["track_list"][0]["track"]["track_id"]
        return str(track_id)

        # Gets track ID from top charts of France (not used)
    def get_track_id_FR():
        url = 'https://api.musixmatch.com/ws/1.1/chart.tracks.get?apikey=69af09eed279453b11832306fcdf0187&chart_name=top&page=1&page_size=5&country=fr&f_has_lyrics=1'
        response = urllib.request.urlopen(url)
        content = response.read().decode()
        content = json.loads(content)
        track_id = content["message"]["body"]["track_list"]["track"]["track_id"]
        return str(track_id)

        # Gets track ID from top charts of world.
    def get_track_id_world():
        url = 'https://api.musixmatch.com/ws/1.1/chart.tracks.get?apikey=69af09eed279453b11832306fcdf0187&chart_name=top&page=1&page_size=5&country=xw&f_has_lyrics=1'
        response = urllib.request.urlopen(url)
        content = response.read().decode()
        content = json.loads(content)
        track_id = content["message"]["body"]["track_list"]["track"]["track_id"]
        return str(track_id)

        # Gets the lyrics from a track
    def find_lyrics():
        track_id = get_track_id()
        url = "https://api.musixmatch.com/ws/1.1/track.lyrics.get?apikey=69af09eed279453b11832306fcdf0187&"\
              + "track_id=" + track_id
        response = urllib.request.urlopen(url)
        content = response.read().decode()
        content = json.loads(content)
        lyrics_body = content["message"]["body"]["lyrics"]["lyrics_body"]
        return lyrics_body

        # Counts the lyrics
    def lyrics_count():
        lyrics = find_lyrics()
        lyric_list = re.sub("[^a-zA-Z0-9_']", " ", lyrics).split()
        amount = Counter(map(str.lower, lyric_list))
        return amount

        # Maps variables 'x' and 'y' to a dictionary of lyrics.
    def bar_graph_format():
        dict = lyrics_count()
        lyric_key = sorted(dict.keys(), key=lambda k: dict[k], reverse=True)
        lyric_freq = []
        lyric_words = []
        frequency = []
        for lyric in lyric_key:
            lyric_freq.append(dict[lyric])
        for i in range(0, 11):  # number after the comma is how many lyrics you want to be included on the graph (minus 1)
            lyric_words.append(lyric_key[i])
            frequency.append(lyric_freq[i])
        data = {"y": frequency, "x": lyric_words}
        return json.dumps(data)

    return bar_graph_format()
