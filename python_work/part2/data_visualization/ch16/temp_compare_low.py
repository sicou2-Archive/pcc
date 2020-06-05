import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename_1 = 'data/sitka_weather_2018_simple.csv'
filename_2 = 'data/death_valley_2018_simple.csv'
# filename_3 = 'data/san_francisco_weather_2018.csv'

with open(filename_1) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates_1, lows_1 = [], []

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            low = int(row[6])
        except ValueError:
            print(f"Temp data missing for {current_date}")
        else:
            dates_1.append(current_date)
            lows_1.append(low)


with open(filename_2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates_2, highs_2, lows_2 = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            low = int(row[5])
        except ValueError:
            print(f"Temp data missing for {current_date}")
        else:
            dates_2.append(current_date)
            lows_2.append(low)


# with open(filename_3) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)

#     dates_3, lows_3 = [], [], []

#     for row in reader:
#         current_date = datetime.strptime(row[2], '%Y-%m-%d')
#         try:
#             low = int(row[6])
#         except ValueError:
#             print(f"Temp data missing for {current_date}")
#         else:
#             dates_3.append(current_date)
#             lows_3.append(low)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates_1, lows_1, c=(0, 0, 1.0), alpha=0.7)
ax.plot(dates_2, lows_2, c=(0, 0.3, 0.8), alpha=0.7)
# ax.plot(dates_3, lows_3, c=(0.2, 0, 0.8), alpha=0.7)

plt.show()
