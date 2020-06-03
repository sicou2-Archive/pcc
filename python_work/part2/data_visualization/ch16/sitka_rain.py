import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename_1 = 'data/sitka_weather_2018_simple.csv'
filename_2 = 'data/death_valley_2018_simple.csv'
with open(filename_1) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates_1, rainfall_1, rain_total_1 = [], [], 0

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rain = float(row[3])
        rain_total_1 += rain
        dates_1.append(current_date)
        rainfall_1.append(rain)


with open(filename_2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates_2, rainfall_2, rain_total_2 = [], [], 0

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rain = float(row[3])
        rain_total_2 += rain

        dates_2.append(current_date)
        rainfall_2.append(rain)
print(rain_total_1, "1")
print(rain_total_2, "2")


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates_1, rainfall_1, linewidth=3)
ax.plot(dates_2, rainfall_2, linewidth=3)

plt.title("Rainfall in Sitka, AK in 2018", fontsize=20)
plt.xlabel("", fontsize=14)
plt.ylabel("Rainfall (in.)", fontsize=14)


plt.show()
