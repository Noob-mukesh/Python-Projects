import urllib.request
import json
text=input("Enter text to translate :- ").replace(" ","")
lang=input("Enter Destination langauge code in which you want to translate :- ")

url=f"https://mukesh-api.vercel.app/translate?query{text}&dist={lang}"
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read().decode('utf-8')

out = json.loads(data)
print(out["results"])

'''ʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇs ғᴏʀ ᴛʀᴀɴsʟᴀᴛɪᴏɴ 

af, am, ar, az, be, bg, bn, bs, ca, ceb, co, cs, cy, da, de, el, en, eo, es,
et, eu, fa, fi, fr, fy, ga, gd, gl, gu, ha, haw, hi, hmn, hr, ht, hu, hy, id, ig, is, it, iw, ja, jw, ka, kk, km, kn, ko, ku, ky, la, lb, lo, lt, lv, mg, mi, mk, ml, mn, mr, ms, mt, my, ne, nl, no, ny, pa, pl, ps, pt, ro, ru, sd, si, sk, sl, sm, sn, so, sq, sr, st, su, sv, sw, ta, te, tg, th, tl, tr, uk, ur, uz, vi, xh, yi, yo, zh, zh_CN, zh_TW, zu'''
