from email import header
import requests

para = {"ComicVer":5,"PageCount":25}
headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Accept-language":"en"
}

r = requests.get("https://www.amazon.in/Tecno-Electric-Storage-7000mAh-Processor/dp/B0B315GFSW?ref_=Oct_DLandingS_D_fe907a50_60&smid=A14CZOWI0VEHLG&th=1",headers=headers)

# print(r.content)
# with open("comic.png","wb") as f:
#     f.write(r.content)
# print(r.status_code)

print(r.text)
# print(r.json()["args"])