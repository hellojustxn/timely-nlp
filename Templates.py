# TODO: Handle abbreviations and delimeters here, you might find the link below useful!
# https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python
templates = [
    "{eventName} - {days} from {startTime} to {endTime}",
    "I will be in {eventName} on {days} from {startTime} to {endTime}",
    "{eventName} {days} {startTime} - {endTime}",
    "{eventName} {days} {startTime} to {endTime}",
    "{eventName} - {days} {startTime} - {endTime}",
    "{eventName}: {days} {startTime} - {endTime}",
]