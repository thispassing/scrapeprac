import requests 

# Make the same request we did two screens ago.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

# Get the response data as a Python object.  Verify that it's a dictionary.
json_data = response.json()
first_pass_duration = json_data['response'][0]['duration']
print("duration value of the ISS' first pass over SF: "+str(first_pass_duration))
print(type(json_data))
print(json_data)