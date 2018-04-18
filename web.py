import requests
import re
import datetime
import time

def alarm_check(time):
         time = re.sub(':','',time)
         time = int(time)
         hour = time /10000
         time = time % 10000
         minute = time /100
         time = time % 100
         sec = time
         if now.hour == hour:
                 ##alarm check succeeded
                 return 1
         return 0

def play_alarm(songid):
        basevol = "http://localhost:5005/Living%20Room/volume/"
        requests.get(basevol+"1")   ##initializes volume to 1
        
        ##begins playing song
        base = "http://localhost:5005/Living%20Room/spotify/now/spotify:track:"
        if songid: ##null checks songid
                final = base+songid 
                r = requests.get(final)

        for v in range(5,100,5):  ##ups volume
                vol = str(v)
                requests.get(basevol+vol) 
                time.sleep(1)





while True:
        now = datetime.datetime.now()

        r = requests.get("http://shrouded-scrubland-66108.herokuapp.com/api/alarms")
        alarms = r.json()

        #iterate through alarms array
        for a in alarms:
                if alarm_check(a['alarm_time']):

                        play_alarm(a['spotifySongID'])


        time.sleep(61-now.second)








