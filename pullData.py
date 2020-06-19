import json
import requests

chimpServer = "https://chimpstagram-upload.glitch.me"
gramEnd = "getgrams"

r = requests.get(chimpServer+'/'+gramEnd)

with open('frog.json', 'w') as outfile:
    json.dump(r.json(), outfile)