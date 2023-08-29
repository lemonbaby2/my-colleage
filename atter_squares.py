# 15.2.4 使用scatter（)绘制散点图并设置样式

import matplotlib.pyplot as plt

plt.style.use('seaborn')  # 样式风格
fig, ax = plt.subplots()    #figure相当于是画板，之后ax是白纸
ax.scatter(2, 4)  # 传递一对X和Y坐标

plt.show()

# 下面设置图表样式，增加标题和给坐标轴上增加标签，确保所有文本都看得清。
import matplotlib.pyplot as plt

plt.style.use('seaborn')  # 样式风格
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)  # 传递一对X和Y坐标

ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)
# 参数axis的值为'x'、'y'、'both'，分别代表设置X轴、Y轴以及同时设置，默认值为'both'。
# ax1.tick_params(axis='x',width=2,colors='gold')
# ax2.tick_params(axis='y',width=2,colors='gold')
# ax3.tick_params(axis='both',width=2,colors='gold')


plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'  # 可能是因为matplotlib的默认字体不支持中文，然后要手动地调为另一种字体.
plt.rcParams['axes.unicode_minus'] = False
plt.show()

# 15.2.6自动计算数据
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
# 设置图表标题并给坐标轴加上标签。
ax.set_title("平方数", fontsize=24)  # 方法set_title绘制图表标题
ax.set_xlabel("值", fontsize=12)  # set_xlabel和set_ylabel绘制每条轴标题
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小。
ax.tick_params(axis='both', which='major', labelsize=14)  # tick_params绘制刻度的样式。

# 设置每个坐标轴的取值范围。
ax.axis([0, 1100, 0, 1100000])

plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'  # 可能是因为matplotlib的默认字体不支持中文，然后要手动地调为另一种字体.
plt.rcParams['axes.unicode_minus'] = False
plt.show()
