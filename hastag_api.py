import urllib.request
import json
input=input("enter text to generate hastag : ")
url=f"https://mukesh-api.vercel.app/hastag?query={input}"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read().decode('utf-8')

out = json.loads(data)
print(out)
