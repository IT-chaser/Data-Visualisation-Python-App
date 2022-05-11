import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

filename = 'data/world_fires_1_day.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get latitude, longitude and brightness from this file.
    lats, lons, bris = [], [], []
    for row in reader:
        lats.append((row[0]))
        lons.append((row[1]))
        bris.append(float(row[2])/10)

# Map the world fires.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [bri/2 for bri in bris],
        'color': bris,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Fire Scale'},
    },
}]
my_layout = Layout(title='Global Fires')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')
