import requests
import re
import datetime

def alarm_check(time):
         time = re.sub(':','',time)
         time = int(time)
         hour = time /10000
         time = time % 10000
         minute = time /100
         time = time % 100
         sec = time
         if now.hour == hour:
                 print('alarm_check true')
                 return 1
         return 0

def play_alarm(songid):
        base = "http://localhost:5005/Living%20Room/spotify/now/spotify:track:"
        if songid:
                final = base+songid ##might give error since songid is null
                print(final);
                r = requests.get(final)


##while 1
#sleep(x)


now = datetime.datetime.now()
##update to every 5 min
r = requests.get("http://shrouded-scrubland-66108.herokuapp.com/api/alarms")
alarms = r.json()



#iterate through alarms array
for a in alarms:
        if alarm_check(a['alarm_time']):
                print('calling play_alarm')
                print(a['spotifySongID'])
                play_alarm(a['spotifySongID'])





