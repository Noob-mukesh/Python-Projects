# Search anything from Wikipedia and get summary of that term
import requests
base_url = "https://mukesh-api.vercel.app/"

class Wikipedia:
    def __init__(self, search_str):
        self.search_str = search_str

    def search_wikipedia(self):
        url = f"{base_url}wikipedia?query={self.search_str}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()["results"]
        else:
            return "Failed to fetch data from Wikipedia."

search_term = input("Search anything on Wikipedia: ")
wikipedia_search = Wikipedia(search_term)
print(wikipedia_search.search_wikipedia())
