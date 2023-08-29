# 同时掷两个骰子时，通常将它们的点数相加。请通过可视化展示将两个骰子的点数相乘的结果。
from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die
# 创建两个D6骰子。
die_1 = Die()
die_2 = Die()
# 掷骰子多次，并将结果存储在一个列表中。
results = []
for roll_num in range(1_000_000):
    result = die_1.roll() * die_2.roll()
    results.append(result)
# 分析结果。
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):

    frequency = results.count(value)
    frequencies.append(frequency)
# 可视化结果。
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of multiplying two D6 dice. (1,000,000 rolls)',
                    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6*d6.html')



