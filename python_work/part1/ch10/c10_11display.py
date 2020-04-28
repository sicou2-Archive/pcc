import json

filename = 'text_files/favorite_number.json'

with open(filename) as f:
    print(json.load(f))