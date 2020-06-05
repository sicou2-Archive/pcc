import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'data/rando_30_day_eq_data.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# readable_file = 'data/readable_eq_data.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    # mag = eq_dict['properties']['mag']
    # lon = eq_dict['geometry']['coordinates'][0]
    # lat = eq_dict['geometry']['coordinates'][1]
    # title = eq_dict['properties']['title']
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])


# print(mags[:10])
# print(lons[:5])
# print(lats[:5])

# Map the earthquakes.
# data = [Scattergeo(lon=lons, lat=lats)]
data = ({
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        'size': [5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },

})
my_layout = Layout(title=all_eq_data['metadata']['title'])

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
