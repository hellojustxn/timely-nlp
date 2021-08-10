#!/usr/bin/python3
import datetime as dt
from typing import List

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
    def __init__(self, name: str, days: List[int], startTime: dt.time, duration: int, year: int, abbreviateDate: int):
        self.name = name
        self.days = days
        self.days_str = ""
        self.startTime = startTime
        self.endTime = (dt.datetime(100,1,1,startTime.hour,startTime.minute,startTime.second) + dt.timedelta(seconds=duration)).time() 
        self.duration = duration
        self.year = year
        self.abbreviateDate = abbreviateDate

        # TODO: Handle abbreviations here for now
        if abbreviateDate == 0:
            daysDict[3] = 'Thursday'
        if abbreviateDate == 1:
            daysDict[3] = 'R'
        if abbreviateDate == 2:
            daysDict[3] = 'Th'
        for i in [daysDict[i] for i in days]:
            if (abbreviateDate == 0): 
                self.days_str += i + ", "
            else:
                self.days_str += i[0:abbreviateDate] + ", "
        self.days_str=self.days_str[:-2]

    def set_days(self, days: List[int]):
        self.days = days
    
    def set_year(self, year: int):
        self.year = year

    def set_start_time(self, startTime: dt):
        self.startTime = startTime

    def set_duration(self, duration: int):
        self.duration = duration
        self.stateTime += dt.timedelta(seconds=duration)
    
    def __str__(self):
        days_str = ""
        for i in self.days:
            days_str += daysDict[i] + ", "
        days_str=days_str[0:len(days_str)-2]
        return self.name + ' - ' + days_str + ' from ' + str(self.startTime) + ' to ' + str(self.endTime)