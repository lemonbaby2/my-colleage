import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares)

plt.show()
# 首先导入模块pyplot,并为其指定别名plt,以免反复输人pyplot。
# (在线示例大多这样做，这里也不例外。)模块pyplot包含很多用于生成图表的函数。
# 我们创建了一个名为squares的列表,在其中存储要用来制作图表的数据。然后,采取了另一种常见的Matplotlib做法-
# -调用函数subplots()(见0)。这个函数可在一张图片中绘制一个或多个图表。变量fig表示整张图片。
# 变量ax表示图片中的各个图表,大多数情况下要使用它。
# 接下来调用方法plot(),它尝试根据给定的数据以有意义的方式绘制图表。
# 函数plt.show()打开Matplotlib查看器并显示绘制的图表,如15-
# 在查看器中,你可缩放和导航图形,还可单击磁盘图标将图表保存起来。

# 15.2.1 修改标签文字和线条粗细

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# 设置图表标题并给坐标轴加上标签。
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=12)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小。
ax.tick_params(axis='both', labelsize=14)

plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'  # 可能是因为matplotlib的默认字体不支持中文，然后要手动地调为另一种字体.
plt.rcParams['axes.unicode_minus'] = False
plt.show()

# 15.2.2校正图形
# 图形更容易看清后,我们发现没有正确地绘制数据:折线图的终点指出4.0的平方为25!下 面来修复这个问题。
# 向plot()提供一系列数时,它假设第一个数据点对应的x坐标值为0,但这里第一个点对应 的x值为1。
# 为改变这种默认行为,可向plot()同时提供输入值和输出值:

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# 设置图表标题并给坐标轴加上标签
# 设置图表标题并给坐标轴加上标签。
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=12)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小。
ax.tick_params(axis='both', labelsize=14)


plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'  # 可能是因为matplotlib的默认字体不支持中文，然后要手动地调为另一种字体.
plt.rcParams['axes.unicode_minus'] = False
plt.show()

# 现在plot()将正确地绘制数据,因为同时提供了输入值和输出值，plot()无须对输出值的生成方式作出假设。
# 使用plot()可指定各种形参，还可使用众多函数对图形进行定制。


# 15.2.3 使用内置样式
# Matplotlib提供定义好的样式，生成可视化的效果。

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)  # 参数linewidth决定了plot（绘制的线条粗细。）

# 设置图表标题并给坐标轴加上标签
# 设置图表标题并给坐标轴加上标签。
ax.set_title("平方数", fontsize=24)  # 方法set_title绘制图表标题
ax.set_xlabel("值", fontsize=12)  # set_xlabel和set_ylabel绘制每条轴标题
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小。
ax.tick_params(axis='both', labelsize=14)  # tick_params绘制刻度的样式。

plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'  # 可能是因为matplotlib的默认字体不支持中文，然后要手动地调为另一种字体.
plt.rcParams['axes.unicode_minus'] = False
plt.show()
