from pyuseragents import random as random_useragent
from requests import Session

print("Софт от лучшего канала - https://t.me/cryptoblinchik")
print("Почты должны быть в виде: email или email:password")
file = input("Введите названия файла с почтами (файл должен находиться в папке с файлом скрипта): ")
with open(file) as f:
    for i in f.readlines():
        email = i.split(":")[0]
        session = Session()
        session.headers.update({'user-agent': random_useragent(),
                                'accept': 'application/json, text/javascript, */*; q=0.01',
                                'accept-language': 'ru,en;q=0.9',
                                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'origin': 'https://info.nickelodeon.xyz',
                                'referer': 'https://info.nickelodeon.xyz/'
                                })
        r = session.post("https://webflow.com/api/v1/form/629f51dbc2807bf67cd0b735",
                         data={"name": "Nickelodeon Drop Email Form",
                               "source": "https://info.nickelodeon.xyz/",
                               "test": "false",
                               "fields[Email]": email,
                               "dolphin": "false"})
        if r.ok:
            print(email, "on the waitlist")