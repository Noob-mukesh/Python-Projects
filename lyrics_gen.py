# Lyrics Generator using selenium python


import requests
from bs4 import BeautifulSoup
from selenium import webdriver  
from selenium.webdriver.common.by import By
song=input("Enter song name : ")
class Lyrics:
    def __init__(self,song) -> None:
        self.song=song
    
    def lyrics_gen(self) :
        driver = webdriver.Chrome()
        driver.get(f"https://genius.com/search?q={self.song}")
        driver.find_element(By.XPATH,"""/html/body/routable-page/ng-outlet/search-results-page/div/div[2]/div[1]/div[1]/search-result-section/div/div[2]/search-result-items/div/search-result-item/div/mini-song-card/a/div[2]""").click()
        page=requests.get(driver.current_url)
        soup = BeautifulSoup(page.content, "html.parser")
        lyrics=soup.find_all("div","Lyrics__Container-sc-1ynbvzw-1 kUgSbL")
        for i in lyrics:
            return i.text
x=Lyrics(song)
print(x.lyrics_gen())
