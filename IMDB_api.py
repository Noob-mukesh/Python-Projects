# Get Movie info from IMDb website

import requests
base_url = "https://mukesh-api.vercel.app/"

class IMDb:
    def __init__(self, search_str):
        self.search_str = search_str

    def search_imdb(self):
        url = f"{base_url}imdb?query={self.search_str}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["results"]
        else:
            return "Failed to fetch data from IMDb."

search_term = input("Search movie info from movie name: ")
imdb_search = IMDb(search_term)
print(imdb_search.search_imdb()) 


