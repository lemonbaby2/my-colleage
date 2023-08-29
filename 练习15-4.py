# 15-4改进的随机漫步



import matplotlib.pyplot as plt
from random_walk import RandomWalk
# 只要程序处于活动状态，就不断地模拟随机漫步。
while True:
    # 创建一个RandomWalk实例。
    rw = RandomWalk(5_000)
    rw.fill_walk()
    # 将RandomWalk实例包含的点都绘制出来。
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, linewidth=1, zorder=1)
    # 突出起点和终点。
    ax.scatter(0, 0, c='green', edgecolors='none', s=100, zorder=2)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    s=100, zorder=2)
    # 隐藏坐标轴。
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
