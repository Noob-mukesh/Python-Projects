
# google image api 


import requests

class GoogleImageAPI:
    """
    A simple class to interact with the Google Image API.
    """

    def __init__(self, base_url):
        """
        Initialize the GoogleImageAPI with the base URL of the API.

        Args:
        base_url (str): The base URL of the API.
        """
        self.base_url = base_url

    def search_images(self, query):
        """
        Retrieve images from Google Image API based on the query.

        Args:
        query (str): The search query for images.

        Returns:
        dict: A dictionary containing the API response.
        """
        endpoint = f"{self.base_url}/googleimg?query={query}"
        headers = {"accept": "application/json"}
        
        response = requests.get(endpoint, headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Failed to retrieve images. Status code: {response.status_code}"}

# Instantiating the class
google_image_api = GoogleImageAPI(base_url="https://mukesh-api.vercel.app")

# Searching for images
result = google_image_api.search_images(query="Boy")
print(result)
