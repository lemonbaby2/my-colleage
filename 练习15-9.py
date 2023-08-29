# 练习15-9 改用列表解析
# 为清晰起见，本节模拟掷骰子的结果时，使用的是较长的for循环。
# 如果你熟悉列表解析，尝试将这些程序中的一个或两个for循环改为列表解析。

from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die
# 创建两个D6骰子。
die_1, die_2 = Die(), Die()
# 掷骰子多次，并将结果存储在一个列表中。
results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]
# 分析结果。
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)] # 列表解析
# 可视化结果。
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 times',
                xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
