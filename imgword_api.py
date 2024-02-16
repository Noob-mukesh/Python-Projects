from PIL import Image
from io import BytesI0
from base64 import b64decode
import requests
url =f"https://mukesh-api.vercel.app/imgword"
r=requests.get(url).json()["results"]
word=requests.get(url).json() ["word"]
x=BytesI0 (b64decode(r))
# u can it directly in tg
print (word)
# to save img
img= Image.open(x)
img.show()
