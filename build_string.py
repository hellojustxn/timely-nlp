#!/usr/bin/python3
import json
import random
import argparse
import re

import sys
from templates import templates

# Generate training data, train.txt, using data.json and templates.py
# TODO: Use argparse instead
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

def writeMultiEvent(groupEvent):
  conjuctions = [" , ", " and ", " // ", " + "]
  # for template in templates:
  res = ""
  for event in groupEvent:
    # Pick a random template
    tmp = templates[random.randint(0,len(templates)-1)].format(eventName=event['eventName'], days=event['daysStr'], startTime=event['startTime'], endTime=event['endTime'], duration=event['duration'], year=event['year'])

    # If the index is not at the last element, do not append "and"
    if (event != groupEvent[-1]):
      res = tmp + conjuctions[random.randint(0, len(conjuctions) - 1)]
    else:
      res = res + tmp
  # print(f"{res}\n\n")
  f.write(f"{res}")

# At most 5 events in a groupEvent
x = re.search("(\d+)", sys.argv[1]).group()
fileName=f"train-{x}.txt"
f = open(fileName, "w")
for groupEvent in data:
    writeMultiEvent(groupEvent)
    if groupEvent != data[-1]:
        f.write(f"\n")
f.close()

print(f"Files generated: {sys.argv[1]}, {fileName}")