from datetime import datetime
from pytz import timezone
import pytz
import time 
import pyautogui
import sys

if len(sys.argv) != 3:
    print("Wrong number of arguments. Expected: 3, got: " + str(len(sys.argv)) + ".")
    sys.exit(1)

target_hour = int(sys.argv[1])
target_minute = int(sys.argv[2])

run = True
print("Running...")
while run:
    pyautogui.moveTo(100, 100, duration = 0.1) 
    time.sleep(5)  
    pyautogui.moveTo(150, 150, duration = 0.1) 
    time.sleep(5)

    date_format='%H:%M'
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('US/Pacific'))
    now = date.strftime(date_format)
    now_split = now.split(':')
    current_hour = int(now_split[0])
    current_minute = int(now_split[1])
    if current_hour >= target_hour and current_minute >= target_minute:
        print("Done.")
        run = False
