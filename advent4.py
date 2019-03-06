import re
import pandas as pd

times = []
with open('input4.txt') as f:
    for line in f:
        times.append(line.replace('[', '').replace('\n', '').split('] '))

times.sort(key=lambda x: x[0])

print(times)

last_match = ''
for time in times:
    match = re.search('#[0-9]*', time[1])
    if match:
        last_match = match.group(0).replace('#', '')
        time.append(last_match)
    else:
        time.append(last_match)

df = pd.DataFrame(data=times, columns=('date_time', 'note', 'guard_id'))
df['date_time'] = pd.to_datetime(df['date_time'], yearfirst=True, format='%Y-%m-%d %H:%M')
