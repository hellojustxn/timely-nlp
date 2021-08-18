#!/usr/bin/python3
from typing import List
import datetime as dt
import json

daysDict = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}
class Event:
    """
    duration in seconds
    """
    def __init__(self, eventName: str, days: List[int], startTime: dt.time, duration: int, year: int):
        self.eventName = eventName
        self.days = [daysDict[d] for d in days]
        self.daysStr = ' '.join(map(str, self.days)).replace(" ", ", ")
        self.startTime = startTime.strftime("%H:%M")
        self.endTime = (dt.datetime(100,1,1,startTime.hour,startTime.minute,startTime.second) + dt.timedelta(seconds=duration)).time().strftime("%H:%M")
        self.duration = duration
        self.year = year

    def set_days(self, days: List[int]):
        self.days = days
    
    def set_year(self, year: int):
        self.year = year

    def set_start_time(self, startTime: dt):
        self.startTime = startTime

    def set_duration(self, duration: int):
        self.duration = duration
        self.stateTime += dt.timedelta(seconds=duration)
    def __str__():
        print("hi")
    def __repr__(self):
        return json.dumps(self.__dict__)