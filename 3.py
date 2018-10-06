import requests

response = requests.get("http://api.open-notify.org/astros.json")

json_data = response.json()
in_space_count = json_data["number"]
print(in_space_count)