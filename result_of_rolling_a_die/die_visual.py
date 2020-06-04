
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die = Die()

results = []
for roll_no in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result', 'dtick':1}
y_axis_config = {'title': 'Frequency of Results'}
my_layout = Layout(title='Result of rolling a D6 die 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')