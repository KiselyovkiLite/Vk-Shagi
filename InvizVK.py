import requests
from config import token

vizible = input('Включить/Выключить нивидимку(1/2)')

if vizible == '1':
    vizible = 'only_me'
elif vizible == '2':
    vizible = 'all'
else:
    print('Надо ввести 1(Включить нивидимку) или 2(Выключить нивидимку)')

user_agent = 'VKAndroidApp/7.7-10445 (Android 11; SDK 30; arm64-v8a; Xiaomi M2003J15SC; ru; 2340x1080)'

req = requests.get(f'https://api.vk.me/method/account.setPrivacy?v=5.109&key=online&value={vizible}&access_token={token}',
                   headers={'User-Agent': user_agent})

if req.text == '{"response":{"category":"only_me"}}':
    print('Нивидимка Включена')
elif req.text == '{"response":{"category":"all"}}':
    print('Нивидимка Выключена')