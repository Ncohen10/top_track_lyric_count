# Top Track Lyric Count #

**This project graphs the frequency of lyrics from the top chartted song of a given country. A pie chart and bar graphed are created to visualize the data.**

#### MusixMatch API ####
* Uses the Musixmatch API to get the lyric data
* The country is determined by the country_code argument in the lyrics.get_lyric_data(country_code) argument in the server.py file
* country_code is set to 'us' by default
* Gets 30% of the lyrics from the lyric body of a track
* This is because the API being used is on the 'free' plan
* The project will still work if you change to a paid API key


