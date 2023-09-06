#https://afeqb71yva.execute-api.us-east-2.amazonaws.com
# make a post request to the api endpoint with the body: "hello world"
import requests
import sys

url = "https://afeqb71yva.execute-api.us-east-2.amazonaws.com/word-count"

payload = sys.argv[1]

headers = {
    'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)