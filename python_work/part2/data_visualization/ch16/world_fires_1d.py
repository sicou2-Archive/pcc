import csv
from datetime import datetime

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

file = 'data/world_fires_1_day.csv'

with open(file) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, lats, lons, brts = [], [], [], []

    for row in reader:
        dates.append(datetime.strptime(row[5], '%Y-%m-%d'))
        lats.append(row[0])
        lons.append(row[1])
        brts.append(row[2])

data = ({
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [(float(brt) / 50) for brt in brts],
    }
})

layout = Layout(title="Fires on Earth on 22 Sept 2018")

fig = {'data': data, 'layout': layout}
offline.plot(fig, filename='data/world_fires_1_day.html')


# print(brts[:40])
# size = [5 * float(brt) for brt in brts]
# print(size[:40])
