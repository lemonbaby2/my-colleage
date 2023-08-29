from matplotlib import pyplot as plt
# 定义数据。
x_values = list(range(5001))
cubes = [x**3 for x in x_values]
# 创建图形。
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, cubes, c=cubes, cmap=plt.cm.Greens, s=10)
# 设置图表名称和坐标轴名称。
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cube of Value', fontsize=14)
# 设置刻度标签的大小以及每个坐标轴的取值范围。
ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 5100, 0, 5100**3])
# 显示图形。
plt.show()
