import json
import requests
import os
#access_token="853851641394176|b09327fcb2c560c8fe211b5720bdf81c"
access_token="CAACEdEose0cBAPqZBJhlt0IW19ZCMaat4ZAlVV8lJa8PbXDmuYZCMWrTUcDhaNK69jcRAU4cqj0L6Wh7DhKZCARqgxHRx1WdPzq4Fq2x3HuK0bXymCJOEQoal0MRK2SuZAEv0Bz2OM7u8NqcKc0kjWwhIioeaxOzl3sNrrY9e5T6r00AKGDbFmqHZBm7qNC89DEf2me7tvf5SBZASw4XIgUO"
search_word="raleigh"
fileW=open("event-id", "w")
def fb_event():
	url = "https://graph.facebook.com/search?q="+search_word+"&type=event&access_token="+access_token
	r = requests.get(url)
	if r.status_code == 200:
		for event in r.json()["data"]:
			#print event["id"]
			fileW.write(event["id"]+"\n")
#			print event
#	with open("json","w") as outfile:
#		json.dump(r.json(), outfile)
fb_event()
fileW.close()
