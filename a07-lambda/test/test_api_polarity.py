#https://8nlij9cme5.execute-api.us-east-2.amazonaws.com
import requests

# Change the endpoint
url_endpoing = "https://8nlij9cme5.execute-api.us-east-2.amazonaws.com"

url = f"{url_endpoing}/polarity"

# Change the phrase
body = {"text": "This was the worst movie I watched this year, horrible!"}

resp = requests.post(url, json=body)

print(f"status code: {resp.status_code}")
print(f"text: {resp.text}")