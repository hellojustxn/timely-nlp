import json
import sys
from sutime import SUTime

if __name__ == '__main__':
    print (len(sys.argv) )

    if len(sys.argv) != 2:
        print("Usage: python3 nlp.py \"Set a meeting tomorrow from 3 to 4PM\"")
        exit(1)
    print (sys.argv[1])
    test_case = sys.argv[1]
    sutime = SUTime(mark_time_ranges=True, include_range=True)
    print(json.dumps(sutime.parse(test_case), sort_keys=True, indent=4))


