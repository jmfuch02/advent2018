import re
import pandas as pd

times = []
with open('input4.txt') as f:
    for line in f:
        times.append(line.replace('[', '').replace('\n', '').split('] '))

times.sort(key=lambda x: x[0])

print(times)

last_match = ''
for event in times:
    # strip off the year
    event[0] = (re.sub('[0-9]{4,}-', '', event[0]))
    # parse time into month, day, hour, minute
    event[0] = re.split(' |:', event[0])
    # get the guard id
    match = re.search('#[0-9]*', event[1])
    if match:
        last_match = match.group(0).replace('#', '')
        event.append(last_match)
    else:
        event.append(last_match)

fmt = []
for event in times:
    print(event)
    date = event[0][0]
    minute = event[0][2]
    desc = event[1]
    print(f'desc: {desc}')
    gid = event[2]

    if 'Guard' not in desc:
        fmt.append([date, gid, desc, minute])


df = pd.DataFrame(data=fmt, columns=('date', 'gid', 'desc', 'minute'))
# df['month_day'] = pd.to_datetime(df['date'], format='%m-%d')

