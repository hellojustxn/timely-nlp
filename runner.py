import datetime
import random
import os
import sys
from Event import Event
from eventNames import eventNames

# Generate a data.json file containing a list of grouped events
if len(sys.argv) != 2:
  print(f"Usage: python3 {sys.argv[0]} <number of events>")
  exit(1)

NUM_EVENTS = int(sys.argv[1])
eventData = []
for i in range(NUM_EVENTS):
  group = []
  # TODO: Include more event names
  # Generate a random start time and duration
  for i in range(0,random.randint(1,2)):
    START_TIME = datetime.time(random.randint(0,23),random.randint(0,59),random.randint(0,59)) # 0-23 hours, 0-60 min, 0-60 sec
    DURATION = random.randint(900,3600) # 900-3600 is 15-60 minutes
    
    # Simulate creating an event with random days by arbitrarily removing days from the week
    days = [0,1,2,3,4,5,6]
    a = datetime.time(random.randint(0,23),random.randint(0,59),random.randint(0,59)) # 0-23 hours, 0-60 min, 0-60 sec
    for k in range(0,random.randint(0,6)):
      target = random.randint(0,6)
      if target in days:
          days.remove(target)

    event = Event(eventName = eventNames[random.randint(0,len(eventNames) - 1)],days = days,
      startTime=START_TIME,duration = DURATION,year = 2021)
    group.append(event)
  eventData.append(group)

now = datetime.datetime.now().strftime("%m%d%S")
fileName = f"data-{now}.json"
f = open(fileName, "w")
f.write(f"{eventData}")
f.close()

os.system(f'python3 build_string.py {fileName}')