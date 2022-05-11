from plotly.graph_objs import Bar, Layout
from plotly import offline

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:

    # Make a random walk.
    rw = RandomWalk(1000)
    rw.fill_walk()

    # Visualize the results.
    data = [Bar(x=rw.x_values, y=rw.y_values)]

    x_axis_config = {'title': 'Result'}
    y_axis_config = {'title': 'Frequency of Result'}
    my_layout = Layout(title='Results of random walk',
            xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({'data': data, 'layout': my_layout}, filename='plotly_rw.html')
    break
