import requests


ask=input(" Ask anything .")
base_url="https://mukesh-api.vercel.app/"
class GoogleBard:
    
    """ Google Bard ai  by @mr_sukkun"""
    def __init__(self, ask) -> None:
        self.chat=ask 
    
    def bard_reply(self) :
        url=f"{base_url}bard?query={self.ask}"
        return requests.get(url).json()["results"]
        
        
        
x=GoogleBard(ask)
print(x.bard_reply())
