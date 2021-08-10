#!/usr/bin/python3
from Templates import templates
from Event import Event
from EventNames import eventNames
import datetime
import random

eventList = []
TOTAL_EVENTS = 100
DURATION = random.randint(900,3600) # 15-60 minutes

# Populate the eventList with events using random days and times
for i in range(0,TOTAL_EVENTS):
    days = [0,1,2,3,4,5,6]
    a = datetime.time(random.randint(0,23),random.randint(0,59),random.randint(0,59)) # 0-23 hours, 0-60 min, 0-60 sec
    for j in range(0,random.randint(0,6)):
        target = random.randint(0,6)
        if target in days:
            days.remove(target)
    event = Event('{0}{1}'.format(eventNames[random.randint(0, len(eventNames) - 1)], random.randint(50, 300)), days, a, DURATION, 2021, abbreviateDate=random.randint(0,3))
    eventList.append(event)

for event in eventList:
    for template in templates:
        print(template.format(
            name=event.name,
            days=event.days_str,
            startTime=event.startTime,
            endTime=event.endTime,
            duration=event.duration,
            year=event.year), end="\n")
