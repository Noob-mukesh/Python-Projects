import urllib.request
import json

url=f"https://mukesh-api.vercel.app/mahadev"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read().decode('utf-8')

out = json.loads(data)
print(out["result"])
