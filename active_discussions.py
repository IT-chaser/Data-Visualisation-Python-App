from operator import itemgetter

import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
labels, comments, titles = [], [], []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    try:
        comment = response_dict['descendants']
    except KeyError:
        comment = 0
    comments.append(comment)

    title = response_dict['title']
    hn_link = f"http://news.ycombinator.com/item?id={submission_id}"
    label = f"{title}<br />{hn_link}"
    labels.append(label)
    titles.append(title)

# Make visualization.
data = [{
    'type': 'bar',
    #'x': titles,
    'y': comments,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6
}]

my_layout = {
    'title': 'Most Active Discussions on Hacker News',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14}
        },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='active_discussions.html')
