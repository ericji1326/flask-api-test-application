import requests
import json

# Example of GET Request
response = requests.get('http://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow')

for question in response.json()['items']:
    print(question['title'])