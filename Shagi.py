import requests
from datetime import datetime
from config import token
print('Взлом вк шагов....начался')
steps = 80000
distance = 50000
if token == '':
    print('Введите токен от страницы')
    token=input()

new_date=input('Сегодняшняя дата?(Y/N)')
if new_date.lower() == 'n':
    date = input('Формат YYYY-MM-DD')
elif new_date.lower() == 'y':
    date = datetime.today().strftime('%Y-%m-%d')
else:
    print('Ладно похуй тебя хуй поймешь давай сегоднящнуюю')
    date = datetime.today().strftime('%Y-%m-%d')
user_agent = 'VKAndroidApp/7.7-10445 (Android 11; SDK 30; arm64-v8a; Xiaomi M2003J15SC; ru; 2340x1080)'

req = requests.get(f'https://api.vk.com/method/vkRun.setSteps?steps={steps}&distance={distance}&date={date}'
                   f'&access_token={token}&v=5.131',headers={'User-Agent': user_agent})

if req.text == '{"response":{"steps":80000,"distance":50000}}':
    print("Взлом успешный иди проверяй шаги")
else:
    print('какая та ошибка короче чота ты накосячил')
    print(req.text)
