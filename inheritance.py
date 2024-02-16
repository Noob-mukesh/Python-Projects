#Inheritance in python

import requests
class GoogleImageAPI:
    """
    A simple class to interact with the Google Image API.
    """

    def __init__(self, base_url):
        self.base_url = base_url

    def search_images(self, query):
    
        endpoint = f"{self.base_url}/googleimg?query={query}"
        headers = {"accept": "application/json"}
        
        response = requests.get(endpoint, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve images. Status code: {response.status_code}"}

class Blackbox(GoogleImageAPI):
    def init(self,base_url):
        super().__init__(base_url)
        
    def blackbox_response(self,query):
        endpoint = f"{self.base_url}/blackbox?query={query}"
        response = requests.get(endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve images. Status code: {response.status_code}"}

bl=Blackbox(base_url="https://mukesh-api.vercel.app")
print(bl.blackbox_response(query="write simple python flask app"))
print(bl.search_images("boy"))
