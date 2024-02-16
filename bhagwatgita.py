import requests
chapter_number=input("enter chapter number between 1-18:->> ")

class BhagwatGita:
    def __init__(self, url):
        self.url = url

    def get_info(self):
        response = requests.get(self.url).json()
        # print(response["chapter_number"], response["verse"], response["chapter_intro"], response["shalok"])
        print(response)


url = f"https://mukesh-api.vercel.app/bhagwatgita?query={chapter_number}"
bhagwat_gita = BhagwatGita(url)
bhagwat_gita.get_info()
