# # 两个D8
# # 编写一个程序，模拟同时掷两个8 面骰子1000 次的结果。
# # 先想象一下结果会是什么样的，再运行这个程序，看看你的直觉准不准。逐渐增加掷骰子的次数，直到系统不堪重负为止。
# from plotly.graph_objs import Bar, Layout
# from plotly import offline
# from die import Die
#
# # 创建两个D8骰子。
# die_1 = Die(8)
# die_2 = Die(8)
# # 掷骰子多次，并将结果存储在一个列表中。
# results = []
# for roll_num in range(1_000_000000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
# # 分析结果。
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# for value in range(2, max_result + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
# # 可视化结果。
# x_values = list(range(2, max_result + 1))
# data = [Bar(x=x_values, y=frequencies)]
# x_axis_config = {'title': 'Result', 'dtick': 1}
# y_axis_config = {'title': 'Frequency of Result'}
# my_layout = Layout(title='Results of rolling two D8 dice 1,000,000 times',
#                    xaxis=x_axis_config, yaxis=y_axis_config)
# offline.plot({'data': data, 'layout': my_layout}, filename='d8_d8.html')

# 15_7
# 同时掷三个骰子
from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(500000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(1, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '结果出现的频率'}

my_layout = Layout(title='掷三个D6 50000次的结果',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='3D6.html')

