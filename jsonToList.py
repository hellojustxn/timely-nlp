import json
import math
import datetime
import re
import sys

# Run python3 jsonToList.py label-082012.json to vectorize labels, outputfile label-082012.txt
# Sample label: [0.52, 0.55, 1, 1, 1, 1, 1, 1, 1]
# [startTime, endTime, M, T, W, R, F, S, S]
# TODO: I am considering normalizing the time to values 0 - 1
# Or converting to seconds, the latter seems to make sense
# However, it may not be best practice
def normalizeTime(timeStr):
  date_time_obj = datetime.datetime.strptime(timeStr, '%H:%M')
  SECONDS_IN_DAY = 86400
  seconds = date_time_obj.hour * 3600
  seconds += date_time_obj.minute * 60
  return round( seconds/SECONDS_IN_DAY, 2)

# TODO: Should probably use from sklearn.preprocessing import MultiLabelBinarizer
def oneHotEncode(d):
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  res = [0]*7
  for count, day in enumerate(days):
    if day in d:
      res[count] = 1
  return res


# TODO: Add event name, but how would you represent this?
# Days should be one hot encoded per 
# https://machinelearningmastery.com/one-hot-encoding-for-categorical-data/
# Event = [days, startTime, endTime]
# Opening JSON file
def main():
  if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <filename.json>")
    exit(1)
  
  f = open(sys.argv[1])
  data = json.load(f)
  labels = []
  for i in data:
    # event = []
    # # event.append(oneHotEncode(i[0]['days']))
    # event.append()
    # event.append()
    # TODO: Should be able to write here 
    # instead of appending to an arr
    # to prevent memory issues
    labels.append([ *[normalizeTime(i[0]['startTime']), normalizeTime(i[0]['endTime'])], *oneHotEncode(i[0]['days'])] )
  f.close()

  x = re.search("(\d+)", sys.argv[1]).group()
  fileName=f"label-{x}.txt"
  fw = open(fileName, "w")
  for label in labels:
    fw.write(f"{label}")
    if (label != labels[-1]):
      fw.write(f"\n")

  fw.close()

  # for i in label:

if __name__ == "__main__":
  main()