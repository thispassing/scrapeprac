import requests

r = requests.get("https://api.twitch.tv/kraken/streams/TFBlade")

print(r.status_code)

#json_data = r.json()
#whatever = json_data[0]
#print(whatever)