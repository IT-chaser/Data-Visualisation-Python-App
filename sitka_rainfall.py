import  csv
from datetime import datetime

import matplotlib.pyplot as plt

#filename = 'data/sitka_weather_2018_simple.csv'
filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and daily rainfall amounts from this file.
    dates, rains = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rain = float(row[3]) * 100
        dates.append(current_date)
        rains.append(rain)
# Plot the daily rain falls.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rains, c='red')

# Format plot.
plt.title("Daily rainfall amounts", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Daily Rainfall amount", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
