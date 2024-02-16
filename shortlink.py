import pyshorteners

link =input("enter the url link")

shortener = pyshorteners.Shortener()
try:
    tiny_link = shortener.tinyurl.short(link)
    print(" shortend url Link :- ", tiny_link)

except:
    print("error  while converting shorts link")
