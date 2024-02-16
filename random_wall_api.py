# get random wallpaper for pc
import requests

base_url="https://mukesh-api.vercel.app/"
class Wallpaper:
    def __init__(self):
        pass
    def wall(self):
        url=f"{base_url}wallpaper"
        return requests.get(url).json()["results"]
H=Wallpaper()
print(H.wall())
#  https://graph.org//file/23edcc969e96d2181d185.jpg
