import requests
import re
import datetime
payload = {"stichwort": "wiki", "ausgabe": "liste"}
r = requests.get("http://shrouded-scrubland-66108.herokuapp.com/api/alarms")
print(r.url)
print(r.status_code)
print(r.encoding)
thing = r.json()
time= thing[0]['alarm_time']
print(time)
time = re.sub(':','',time)
time = int(time)
print(time)
hour = time /10000
time = time % 10000
minute = time /100
time = time % 100
sec = time
print(hour)
print(minute)
print(sec)

now = datetime.datetime.now()
print(now)
if now.hour+10 == hour:
        print('fuck off')


# http://www.example.org/suche?stichwort=wiki&ausgabe=liste
