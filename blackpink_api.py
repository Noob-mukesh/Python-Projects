import requests
from io import BytesIO
from PIL import Image 
from base64 import b64decode

text=input(" enter text to make blackpink .")

class BlackPink:
    base_url="https://mukesh-api.vercel.app/"
    """ Google Bard ai  by @mr_sukkun"""
    def __init__(self, text) -> None:
        self.chat=text
    
    def pink_reply(self) :
        url=f"{base_url}blackpink/{self.text}"
        res=requests.get(url).json()["results"]
        photo=BytesIO(b64decode(res.encode("utf-8")))
        return photo
        #x=Image.open(photo)
        #x.save("mukesh35.png")
        
        
        
x=BlackPink(ask)
print(x.pink_reply())


# #  BlackPink  using Mukesh- Api (https://mukesh-api.vercel.app/)
# Join :- @Python_Codes_Pro

# Support group : @python_group_pro