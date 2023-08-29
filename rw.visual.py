# 1.给点着色
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步。
while True:
    # 创建一个RandomWalk实例。
    rw = RandomWalk()
    rw.fill_walk()
    # 将所有点都绘制出来。
    plt.style.use('classic')
    fig, ax = plt.subplots()

    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=15)  # s代表size
    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break
# 在0处,使用range()生成了一个数字列表,其中包含的数与漫步包含的点数量相同。
# 接下来,将这个列表存储在point_numbers中,以便后面使用它来设置每个漫步点的颜色。
# 将参数c设置为point_numbers,指定使用颜色映射Blues,并传递实参edgecolors='none'以删除每个点周围的轮廓。
# 最终的随机漫步图从浅蓝色渐变为深蓝色.


# 2.重新绘制起点和终点.
import matplotlib.pyplot as plt
from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步。
while True:
    # 创建一个RandomWalk实例。
    rw = RandomWalk()
    rw.fill_walk()
    # 将所有点都绘制出来。
    plt.style.use('classic')
    fig, ax = plt.subplots()

    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=15)  # s代表size,edgecolors='none' 以删除每一个点的轮廓。最终随机漫步图从浅蓝色渐变为、深蓝色
    # 为突出终点,在漫步包含 的最后一个x值和y值处绘制一个点,将其颜色设置为红色,并将尺寸设置为 100。
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
               s=100)


    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break
#
# # 为突出起点,使用绿色绘制点(0,0),并使其比其他点大(s=100)。
# # 为突出终点,在漫步包含 的最后一个x值和y值处绘制一个点,将其颜色设置为红色,并将尺寸设置为 100。
# # 务必将这些代码放在调用plt.show()的代码前面,确保在其他点之上绘制起点和终点。
# # 如果现在运行这些代码,将能准确地知道每次随机漫步的起点和终点。(如果起点和终点不明显,请调整颜色和大小,直到明显为止）




import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50_000)  # 增加点数
    rw.fill_walk()
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9), dpi=64) # 5 调整尺寸以适合屏幕。
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none',
               s=1)  # Colormap，可以理解为一种配色方案

    ax.scatter(0, 0, c='red', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='orange', edgecolors='none', s=100)
    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    plt.show()

    keep_running = input("Make another walk？(y/n):")
    if keep_running == 'n':
        break

