import requests

base_url="https://mukesh-api.vercel.app/"

class Flirt:

     'Random flirt msg'
     def __init__(self):

        pass
     def flirt(self):

        url=f"{base_url}flirt"
        return requests.get(url).json()["results"][0]

H=Flirt()

print(H.flirt())
#Output:
'Do you have a sunburn, or are you always this hot? 🔥😏'

# Random flirt msg