import requests
base_url="https://mukesh-api.vercel.app/"

chat=input("Say something: ")

class Chatbot:
   """ Chatbot by @Mr_sukkun """
   def __init__(self,chat) -> None:
        self.chat=chat
   def chat_reply(self) :
        url=f"{base_url}chatbot?query={self.chat}"
        return requests.get(url).json()["results"]
        
        
        
x=Chatbot(chat)
print(x.chat_reply())
