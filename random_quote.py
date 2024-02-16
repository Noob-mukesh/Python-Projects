# Random quotes using python.

import requests
url="https://mukesh-api.vercel.app/randomquotes"
print(requests.get(url).json()["results"]) 
# Result :
# Friendship is always a sweet responsibility, never an opportunity.