import json

# Explore the structure of the data.
filename = 'data/all_month_2020_03.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'data/readable_file_for_eq_2020_03.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
