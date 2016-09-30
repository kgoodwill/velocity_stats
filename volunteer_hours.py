import sys
import re
import concurrent.futures
import datetime

""" Trying to make this multi-threaded, multiple files or mulitple threads executing on the same file. Either way the results will be in the same place. """

file = open(sys.argv[1], 'r')

volunteers = {}
total_hours = 0

def get_stats(line):
    # Futures will execute this function, use it to generate all stats

    # print(line)
    results = {}
    match = re.search(r'([0-9/]+) ([0-9:]+),([A-Za-z ]+),([A-Za-z ]+),([0-9/]+),([0-9\.]+)', line)
    # If it doesn't match the regex skip it, not worth parsing
    if match == None:
        return results
    timestamp = match.group(1) + " " + match.group(2)
    first_name = match.group(3)
    last_name = match.group(4)
    volunteer_date = match.group(5)
    hours_volunteered = match.group(6)

    results = {
        'timestamp': timestamp,
        'first_name': first_name,
        'last_name': last_name,
        'volunteer_date': volunteer_date,
        'hours_volunteered': hours_volunteered,
    }
    return results

start = datetime.datetime.now()
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
    # Creates a map instead of using map()
    future_to_line = {executor.submit(get_stats, line): line for line in file}
    for future in concurrent.futures.as_completed(future_to_line):
        line = future_to_line[future]
        try:
            data = future.result()
        except Exception as e:
            print('%r generated an exception: %s' % (line, e))
        else:
            # Do something with the returned data
            if future.done():
                x = 1
                # print('---Future Done---')
end = datetime.datetime.now()
print('Execution time: %d microseconds' % (end - start).microseconds)
    # total_hours += float(hours_volunteered)

    # volunteer_name = first_name.lower() + last_name.lower()

#     if volunteer_name in volunteers.keys():
#         volunteers[volunteer_name] += 1
#     else:
#         volunteers[volunteer_name] = 1
#
# unique_volunteers = len(volunteers.keys())
# print('Number of Unique Volunteers: ' + str(unique_volunteers))
# print('Total Hours for all Volunteers: ' + str(total_hours))
