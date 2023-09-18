import requests
import sys

url = "http://localhost:9500/2023-09-12/functions/function/invocations"

payload = sys.argv[1]

headers = {
    'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)