# 1.首先导入pyplot模块。，命名为plt
# 2.把要绘制其函数的一列整数传给plot（）函数
# 3.使用show（）显示函数
import matplotlib.pyplot as plt
import numpy as np
import random

from pylab import mpl

# 设置显示中文字体,用来正常显示中文标签
mpl.rcParams["font.sans-serif"] = ['SimHei']
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False
#
#
#
# plt.plot([1, 2, 3, 4], linestyle='--')
# plt.plot([1, 2, 3, 4], marker='o')
# plt.grid(linestyle='--')
#
# # 图形属性：轴长与输入范围：
# plt.axis([0, 5, 0, 20])  # （xmin xmax ymin ymax）
# plt.xlim([0, 5])
# plt.ylim([0, 20])
#
# # 标题 ，轴标题：
# plt.title("一个简单图形")
# plt.xlabel("x label")
# plt.ylabel("y label")
# #设置中文乱码问题
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.show()
#
# # 图形属性：图例
# plt.plot([1, 2, 3, 4], label='label')
# plt.legend()
# # 显示图例
# plt.legend(loc="best")
# plt.show()
#
# # 图形属性：文本
# plt.plot([1, 2, 3, 4], 'ro', label='label')
# plt.text(1, 2, 'First')
# plt.text(2, 3, 'Second')
# plt.title("A simple title")
# plt.xlabel("x label")
# plt.ylabel("y label")
#
#
# # 网格
# plt.plot([1, 2, 3, 4], [1, 2, 3, 4], 'ro', label='label')
#
# plt.grid(True, linestyle='--', color='r', alpha=0.5)
# # 刻度
# value = [1.5, 2.5, 3.5, 4.5]
# label = ['aa', 'bb', 'cc', 'dd']
# plt.xticks(value, label)
# plt.title("A simple title")
# plt.xlabel("x label")
# plt.ylabel("y label")
#
#
# # 2D绘图——线型图
# x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
# y = np.sin(x * 3) / x
# plt.plot(x, y)
#
#
# # 直方图
# data = np.random.randint(0, 100, 100)
# plt.hist(data, bins=20) #hist组织
#
#
# # 条形图
# index = [0, 1, 2, 3, 4]
# values = [5, 7, 3, 4, 6]
# plt.bar(index, values)
#
#
# # 水平条形图
# index = np.arange(5)
# values1 = [5, 7, 3, 4, 6]
# std1 = [0.8, 1, 0.4, 0.9, 1.3]
# plt.barh(index, values1, xerr=std1, error_kw={'ecolor': '0.1', 'capsize': 6}, alpha=0.7, label='First')
# plt.yticks(index, ['A', 'B', 'C', 'D', 'E'])


# 添加自定义x,y刻度
# 增加以下两行代码
# 构造x轴刻度标签（自定义）
# x_ticks_label = ["11点{}分".format(i) for i in x]
# 构造y轴刻度
# y_ticks = range(40)
# 修改x,y轴坐标的刻度显示
# plt.xticks(x[::5], x_ticks_label[::5])
# plt.yticks(y_ticks[::5])

# 正弦函数和余弦函数
x1 = np.linspace(0, 10, 200)
y1 = np.sin(x1)
plt.plot(x1, y1)
y2 = np.cos(x1)
plt.plot(x1, y2)
plt.show()

plt.subplot(2, 1, 1)
plt.plot(x1, y1)
plt.subplot(2, 1, 2)
plt.plot(x1, y2)
plt.show()

# 使用scatter画10种大小100种颜色的散点图

# 画10种大小，100种颜色的散点图
np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
size = np.random.rand(100) * 1000  # 也就是说我们我们在生成随机数的时候需要让生成的数量保持一致
plt.scatter(x, y, c=colors, s=size, alpha=0.7)
plt.show()

# 不同种类不同颜色的线并添加图例
# 不同种类不同颜色的线并添加图例
x = np.linspace(0, 10, 100)
plt.plot(x, x + 0, '-g', label='-g')  # 实线  绿色
plt.plot(x, x + 1, '--c', label='--c')  # 虚线 浅蓝色
plt.plot(x, x + 2, '-.k', label='-.k')  # 点划线 黑色
plt.plot(x, x + 3, '-r', label='-r')  # 实线  红色
plt.plot(x, x + 4, 'o', label='o')  # 点   默认是蓝色
plt.plot(x, x + 5, 'x', label='x')  # 叉叉  默认是蓝色
plt.plot(x, x + 6, 'dr', label='dr')  # 砖石  红色
# 添加图例右下角 lower right  左上角upper left 边框  透明度  阴影  边框宽度
plt.legend(loc='lower right', fancybox=True, framealpha=1, shadow=True, borderpad=1)
plt.show()

# 柱形图绘制
# Parameters:
# x : 需要传递的数据
#
# width : 柱状图的宽度
# align : 每个柱状图的位置对齐方式
# 	{‘center’, ‘edge’}, optional, default: ‘center’
#
# **kwargs :
# color:选择柱状图的颜色
x = [1980, 1985, 1990, 1995]
x_labels = ['1980年', '1985年', '1990年', '1995年']
y = [1000, 3000, 4000, 5000]
plt.bar(x, y, width=3)

plt.xticks(x, x_labels)
plt.xlabel('年份')
plt.ylabel('销量')
plt.title('根据年份销量对比图')
plt.show()

# 使用bar和barh绘制柱状图
# api：plt.bar(x, width, align='center', **kwargs)
# Parameters:
# x : 需要传递的数据
#
# width : 柱状图的宽度
# align : 每个柱状图的位置对齐方式
# 	{‘center’, ‘edge’}, optional, default: ‘center’
#
# **kwargs :
# color:选择柱状图的颜色

np.random.seed(0)
x = np.arange(5)
y = np.random.randint(-5, 5, 5)
print(x, y)
# 将画布分隔成一行两列
plt.subplot(1, 2, 1)
# 在第一列中画图
v_bar = plt.bar(x, y)
# 在第一列的画布中 0位置画一条蓝线
plt.axhline(0, color='blue', linewidth=2)
plt.subplot(1, 2, 2)
# barh将y和x轴对换 竖着方向为x轴
h_bar = plt.barh(x, y, color='red')
# 在第二列的画布中0位置处画红色的线
plt.axvline(0, color='red', linewidth=2)
plt.show()

# 对部分柱状图，使用颜色区分

np.random.seed(0)
x = np.arange(5)
y = np.random.randint(-5, 5, 5)
v_bar = plt.bar(x, y, color='lightblue')
for bar, height in zip(v_bar, y):
    if height < 0:
        bar.set(edgecolor='darkred', color='lightgreen', linewidth='3')
plt.show()

# 绘制饼状图
# api：plt.pie(x, labels=,autopct=,colors)
# Parameters:
# x:数量，自动算百分比
# labels:每部分名称
# autopct:占比显示指定%1.2f%%
# colors:每部分颜色

# 导入模块
import matplotlib.pyplot as plt
import numpy as np

# 准备男、女的人数及比例
man = 71351
woman = 68187
man_perc = man / (woman + man)
woman_perc = woman / (woman + man)
# 添加名称
labels = ['男', '女']
# 添加颜色
colors = ['blue', 'red']
# 绘制饼状图  pie
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# labels 名称 colors：颜色，explode=分裂  autopct显示百分比
paches, texts, autotexts = plt.pie([man_perc, woman_perc], labels=labels, colors=colors, explode=(0, 0.05),
                                   autopct='%0.1f%%')

# 设置饼状图中的字体颜色
for text in autotexts:
    text.set_color('white')

# 设置字体大小
for text in texts + autotexts:
    text.set_fontsize(20)
plt.show()

# 绘制直方图
# api：matplotlib.pyplot.hist(x, bins=None)
# Parameters:
# x : 需要传递的数据
# bins : 组距


# 使用randn函数生成1000个正态分布的随机数，使用hist函数绘制这1000个随机数的分布状态
import numpy as np
import matplotlib.pyplot as plt

# 频次直方图，均匀分布
# 正太分布
x = np.random.randn(1000)
# 画正太分布图
# plt.hist(x)
plt.hist(x, bins=100)  # 装箱的操作，将10个柱装到一起及修改柱的宽度

# 使用normal函数生成1000个正态分布的随机数，使用hist函数绘制这100个随机数的分布状态
import numpy as np
import matplotlib.pyplot as plt

# 几个直方图画到一个画布中,第一个参数期望  第二个均值
x1 = np.random.normal(0, 0.8, 1000)
x2 = np.random.normal(-2, 1, 1000)
x3 = np.random.normal(3, 2, 1000)
# 参数分别是bins：装箱，alpha：透明度
kwargs = dict(bins=100, alpha=0.4)  # 字典，作为传参使用
plt.hist(x1, **kwargs)
plt.hist(x2, **kwargs)
plt.hist(x3, **kwargs)
plt.show()
