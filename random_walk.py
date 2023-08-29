# 15.3 随机漫步（模拟现实世界很多情形）
# 15.3.1 创建Randomwalk类
# 为模拟随机漫步,将创建一个名为RandomWalk的类,它随机地选择前进方向。
# 这个类需要三个属性:一个是存储随机漫步次数的变量,其他两个是列表,分别存储随机漫步经过的每个点的x坐标和y坐标。
# RandomWalk类只包含两个方法:方法init()和fill_walk(),后者计算随机漫步经过的所有点。先来看看_init_().

from random import choice


class RandomWalk:
    """生成一个随机漫步数据的类。"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性。"""
        self.num_points = num_points

        # 所有随机漫步都始于（0，0）。
        self.x_values = [0]
        self.y_values = [0]

    # 为做出随机决策, 将所有可能的选择都存储在一个列表中, 并在每次决策时都使用模块random中的choice()来决定使用哪种选择(见0)。
    # 接下来, 将随机漫步包含的默认点数设置为5000。这个数大到足以生成有趣的模式, 又小到可确保能够快速地模拟随机漫步(见0)。
    # 然后，在0处创建两个用于存储x值和y值的列表, 并让每次漫步都从点(0, 0)出发。
    # 我们将使用方法fillwalk()来生成漫步包含的点并决定每次漫步的方向, 如下所示。请将这个方法添加到random_walk.py中:


    # 15.3.2 选择方向（将用fill_walk()来生成漫步包含的点并决定每次漫步的方向）
    def fill_walk(self):
        """计算随机漫步的所有点。"""

        # 不断漫步，直到列表表达到指定的长度。
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿着这个方向前进的距离。·
            x_direction = choice([1, -1])

            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([0, 1, 2, 3, 4])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步。
            if x_step == 0 and y_step == 0:
                continue
            # 计算下一个点的x值和y值。
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
#  Q处建立了一个循环,它不断运行,直到漫步包含所需的点数。
# 方法fill walk())的主要部分告诉Python如何模拟四种漫步决定:向右走还是向左走?沿指定的方向走多远?向上走还是向下走?沿选定的方向走多远?
# 使用choice([1,-1])给x direction选择一个值,结果要么是表示向右走的1,要么是表示 向左走的-1 (见R)。
# 接下来, choice([0, 1,2,3,4])随机地选择一个0~4的整数,告诉Python 沿指定的方向走多远(x distance)。
# 通过包含0,不仅能够同时沿两个轴移动,还能够只沿一个 轴移动。
# 在 S 和 T处,将移动方向乘以移动距离,确定沿x轴和y轴移动的距离。
# 如果x_step为正将 向右移动,为负将向左移动,为零将垂直移动;如果y_step为正将向上移动,为负将向下移动,为零将水平移动。
# 如果x_step和y_step都为零,则意味着原地踏步。我们拒绝这样的情况,接着执行下一次循环(见)。
# 为获取漫步中下一个点的x值,将x_step与x_values中的最后一个值相加(见W),对y值 也做相同的处理。
# 获得下一个点的x值和y值后,将它们分别附加到列表x_values和y_values 的末尾。

