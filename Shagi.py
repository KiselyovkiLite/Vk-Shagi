from urllib import request
from datetime import datetime
steps = 80000
distance = 50000
date = datetime.today().strftime('%Y-%m-%d')
access_token = 'cf916985f2217d657632794548337fb588f6389691874a87d736dec92012955744fe81ed59e3ed4d834bf'
user_agent = 'VKAndroidApp/7.7-10445 (Android 11; SDK 30; arm64-v8a; Xiaomi M2003J15SC; ru; 2340x1080)'
print(request.urlopen(request.Request('https://api.vk.com/method/vkRun.setSteps?steps='+str(steps)+'&distance='+str(distance)+'&date='+date+'&access_token='+access_token+'&v=5.131', headers={'User-Agent': user_agent})).read().decode('utf-8'))
