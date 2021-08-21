#!/usr/bin/python3
import json
import random
import argparse
import re
import sys
from templates import templates

# Generate training data, train.txt, using data.json and templates.py
# TODO: Use argparse instead if we decide to add more features
# parser = argparse.ArgumentParser(description='Name of the data file')
# parser.add_argument('string', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
# parser.add_argument('--sum', dest='accumulate', action='store_const',
#                     const=sum, default=max,
#                     help='sum the integers (default: find the max)')
# args = parser.parse_args()
# print(args.accumulate(args.integers))

if len(sys.argv) != 2:
  print(f"Usage: python3 {sys.argv[0]} <filename>")
  exit(1)
  
j = open(sys.argv[1])
data = json.load(j)

def abbrev(s):
  return s[0:2]

def abbreviateDays(daysStr, abbreviateDate):
  splitDays = daysStr.replace(' ', '').split(',')
  for index, day in enumerate(splitDays):
    if (day == 'Thursday' and abbreviateDate == 1):
        splitDays[index] = 'R'
    elif (day == 'Thursday' and abbreviateDate == 2):
        splitDays[index] = 'Th'        
    else:
      if abbreviateDate == 0:
        splitDays[index] = day
      else:
        splitDays[index] = day[0:abbreviateDate]
  return ' '.join(map(str, splitDays)).replace(" ", ", ")

def writeMultiEvent(groupEvent):
  conjuctions = [" , ", " and ", " // ", " + "]
  # for template in templates:
  res = ""
  abbreviateDate = random.randint(0, 3)
  for event in groupEvent:
    # Pick a random template
    # TODO: Change daysstr to days call abbrev to traverse over the arr and build a string
    daysStr_cpy = abbreviateDays(event['daysStr'], abbreviateDate)
    tmp = templates[random.randint(0,len(templates)-1)].format(eventName=event['eventName'], days=daysStr_cpy, startTime=event['startTime'], endTime=event['endTime'], duration=event['duration'], year=event['year'])
    # If the index is not at the last element, do not append "and"
    if (event != groupEvent[-1]):
      res = tmp + conjuctions[random.randint(0, len(conjuctions) - 1)]
    else:
      res = res + tmp
  f.write(f"{res}")

x = re.search("(\d+)", sys.argv[1]).group()
fileName=f"train-{x}.txt"
f = open(fileName, "w")
for groupEvent in data:
    writeMultiEvent(groupEvent)
    if (groupEvent != data[-1]):
      f.write(f"\n")
f.close()

print(f"Files generated: {sys.argv[1]}, {fileName}")
