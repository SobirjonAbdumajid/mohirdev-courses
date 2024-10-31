# import json
# import googlemaps
# from apikey import APIKEY

# gmaps = googlemaps.Clint(key=APIKEY)

# data = gmaps.geocode('Olmazor', 'Tashkent', 'Uzbekiston')

# g = json.dumps(data[0], indent=4, sort_keys=True)
# print(g)

# import json
# import googlemaps
# from apikey import APIKEY

# # Initialize the Google Maps client with your API key
# gmaps = googlemaps.Client(key=APIKEY)

# # Geocode the address
# data = gmaps.geocode('Olmazor, Tashkent, Uzbekistan')

# # Format the data as JSON and print it
# g = json.dumps(data[0], indent=4, sort_keys=True)
# print(g)


# import json
# import requests

# wikiurl = 'https://w3schools.com/python/demopage.htm'
# response = requests.get(wikiurl)
# print(json.dumps(response[0], indent=4, sort_keys=1))
# # with open('somsajon', 'w', encoding='utf-8') as file:
# #     file.write(str((response.text)))

import json

bemor = {
    "name": "Bob",
    "age": 25,
    "oila": True,
    "farzandlar": ("ahmad", "toshmat"),
    "arlergiyasi" : None,
    "dorilar": [
        {"nome": "Analgin", "miqdori": 0.5},
        {"nome": "Alergy", "miqdori": 1.5}
    ],
    "city": "San Francisco",
    "occupation": "Designer",
    "hobbies": ["photography", "traveling", "painting"]
}

sonlar = [2,3,4,5]

bemor_json = json.dumps(bemor, indent=4) # dumps uses for converting to json
# print(bemor.keys())
# print(bemor['dorilar'])
# print(bemor['dorilar'][1]['nome'])
# print(bemor['dorilar'][1].keys())
# print(type(bemor))
# print(type(bemor_json))
print(bemor_json)

bemor2 = json.loads(bemor_json)
print(bemor2)

# with open('jsonjon.json', 'w') as f:
#     json.dump(bemor, f)