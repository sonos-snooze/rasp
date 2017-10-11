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
         if now.hour == hour:  ##adjust later to actually reflect proper check
                 print('alarm_check true')
                 return 1
         return 0

def play_alarm(songid):
        basevol = "http://localhost:5005/Living%20Room/volume/"
        requests.get(basevol+"1")   ##initializes volume to 1
        
        ##begins playing song
        base = "http://localhost:5005/Living%20Room/spotify/now/spotify:track:"
        if songid: ##null checks songid
                final = base+songid ##might give error since songid is null
                print(final);
                r = requests.get(final)

        for v in range(5,100,5):  ##ups volume
                vol = str(v)
                requests.get(basevol+vol) 
                time.sleep(1)





while True:
        now = datetime.datetime.now()
        print(now)
        print(now.second)
        print(now.minute)

        ##update to every 5 min (necessary? possible but not sure if necessary)
        r = requests.get("http://shrouded-scrubland-66108.herokuapp.com/api/alarms")
        alarms = r.json()


        #iterate through alarms array
        for a in alarms:
                if alarm_check(a['alarm_time']):
                        print('calling play_alarm')
                        print(a['spotifySongID'])
                        play_alarm(a['spotifySongID'])


        time.sleep(61-now.second)








