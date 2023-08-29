# 15.6 同时掷两个骰子
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 创建两个D6
die_1 = Die()
die_2 = Die()

results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]  # 用于绘制条形图的Bar类

x_axis_config = {'title': '结果', 'dtick': 1}           # 设置字典,dtick键显示刻度间距，'dtick': 1让Ploty显示每个刻度值
y_axis_config = {'title': '结果的频率'}                  # 设置字典
my_layout = Layout(title='掷两个D6 1000次结果',           # Layout()返回一个指定图表布局和配置的对象。传入x轴和y轴的字典
                   xaxis=x_axis_config, yaxis=y_axis_config)   # 这里设置了图表名称,并传人了x轴和y轴的配置字典。

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')
# 函数 offline.plot()，这个函数需要一个包含数据和布局对象的字典,还接受一个文件名,指定要将图表保存到哪里.



