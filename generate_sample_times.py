#!/usr/bin/python3
from Templates import templates
from Event import Event
from EventNames import eventNames
import datetime
import random

eventList = []
TOTAL_EVENTS = 100
DURATION = random.randint(900,3600) # 15-60 minutes
delimiters = ["; ", " and "]


# Populate the eventList with events using random days and times
for i in range(0,TOTAL_EVENTS):
    # Generate a list of 1-5 events
    multEvent = []
    for j in range(0, random.randint(1, 5)):
        days = [0,1,2,3,4,5,6]
        a = datetime.time(random.randint(0,23),random.randint(0,59),random.randint(0,59)) # 0-23 hours, 0-60 min, 0-60 sec
        for k in range(0,random.randint(0,6)):
            target = random.randint(0,6)
            if target in days:
                days.remove(target)
        event = Event('{0}{1}'.format(eventNames[random.randint(0, len(eventNames) - 1)], random.randint(50, 300)), days, a, DURATION, 2021, abbreviateDate=random.randint(0,3))
        multEvent.append(event)
    eventList.append(multEvent)


# Print multiple time ranges on the same line with the same template
for multEvent in eventList:
    for template in templates:
        # Add test cases for events separated by "; " and " and "
        for delimiter in delimiters:
            # If printing the last time range in the event, end with a new line, otherwise, the randomly decided delimiter
            for count, event in enumerate(multEvent):           
                if(count == len(multEvent)-1):
                    ending = "\n"
                else:
                    ending = delimiter

                # Randomize between using military time or AM/PM
                if(random.randint(0, 1)):
                    eventStartTime = event.startTime.strftime("%I:%M %p")
                    eventEndTime = event.endTime.strftime("%I:%M %p")
                else:
                    eventStartTime = event.startTime
                    eventEndTime = event.endTime

                # Chance for single letter abbreviations to not be separated by a comma (MWF instead of M, W, F)
                eventDays = event.days_str
                if(event.abbreviateDate == 1):
                    if(random.randint(0, 1)):
                        eventDays = event.days_str.replace(", ", "")

                print(template.format(
                    name=event.name,
                    days=eventDays,
                    startTime=eventStartTime,
                    endTime=eventEndTime,
                    duration=event.duration,
                    year=event.year), end=ending)
