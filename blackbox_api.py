#blackbox api
import requests

class Blackbox:
    """
    A class to interact with the Blackbox API.

    Attributes:
    base_url (str): The base URL of the Blackbox API.
    """
    def __init__(self):
        self.base_url = "https://mukesh-api.vercel.app/blackbox"

    def make_request(self, query):
        """
        Makes a request to the Blackbox API with the provided query.

        Args:
        query (str): The query string to send to the API.

        Returns:
        dict: The JSON response from the API.
        @mr_sukkun
        """
        url = f"{self.base_url}?query={query}"
        headers = {
            "accept": "application/json"
        }
        response = requests.get(url, headers=headers)
        return response.json()

# Example usage
box = Blackbox()
result = box.make_request("hi")
print(result)
