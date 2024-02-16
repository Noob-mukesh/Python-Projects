# Getter and Setters in Python
import requests

class MukeshAPI:
    """
    A simple class to interact with the API.
    """
    def __init__(self, base_url="https://mukesh-api.vercel.app",endpoint=""):
        self._base_url = base_url
        self._endpoint=endpoint
    @property
    def endpoint(self):
        return self._endpoint
    @endpoint.setter
    def endpoint(self, new_endpoint):
        self._endpoint = new_endpoint

    def search(self, query):
        url = f"{self._base_url}/{self.endpoint}?query={query}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()["results"]
        else:
            return {"error": f"Failed to retrieve. Status code: {response.status_code}"}
    def search2(self):
        url = f"{self._base_url}/{self.endpoint}"
        headers = {"accept": "application/json"}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()["results"]
        else:
            return {"error": f"Failed to retrieve. Status code: {response.status_code}"}
    def search3(self,api_key, query):
        url = f"{self._base_url}/{self.endpoint}?query={query}"
        headers = {"accept": "application/json","Api-Key":api_key}
        response = requests.post(url, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve. Status code: {response.status_code}"}

bl=MukeshAPI(endpoint="bhagwatgita")
print(bl.endpoint)
print(bl.search3(api_key="get from @adventure_robot",query=1))
bl.endpoint="truth"
print(bl.endpoint)
print(bl.search2())
bl.endpoint = "chatgpt"
print(bl.endpoint)
print(bl.search("write basic website code using html and css"))
