import requests
import json


# put your keys in the header
headers = {
    "app_id": "5b8b9491",
    "app_key": "51d177e8f5316049ae4a5d209c5af117"
}

payload = '{"image":"images/shravan.jpg"}'

url = "http://api.kairos.com/detect"

# make request
r = requests.post(url, data=payload, headers=headers)
data = r.json()

print (data)