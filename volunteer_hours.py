import sys
import re
import datetime

file = open(sys.argv[1], 'r')

volunteers = {}
total_hours = 0

start = datetime.datetime.now()
for line in file:
    # print(line)
    match = re.search(r'([0-9/]+) ([0-9:]+),([A-Za-z ]+),([A-Za-z ]+),([0-9/]+),([0-9\.]+)', line)
    # If it doesn't match the regex skip it, not worth parsing
    if match == None:
        continue
    timestamp = match.group(1) + " " + match.group(2)
    first_name = match.group(3)
    last_name = match.group(4)
    volunteer_date = match.group(5)
    hours_volunteered = match.group(6)

    total_hours += float(hours_volunteered)

    volunteer_name = first_name.lower() + last_name.lower()

    if volunteer_name in volunteers.keys():
        volunteers[volunteer_name] += 1
    else:
        volunteers[volunteer_name] = 1

unique_volunteers = len(volunteers.keys())
print('Number of Unique Volunteers: ' + str(unique_volunteers))
print('Total Hours for all Volunteers: ' + str(total_hours))

end = datetime.datetime.now()
print('Execution time: %d microseconds' % (end - start).microseconds)
