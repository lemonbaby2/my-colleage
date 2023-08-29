# 15.4.2 创建Die类

# 模拟旨一个骰子的情况
from random import randint


class Die:
    """表示一个骰子的类."""

    def __init__(self, num_sides=6):
        """骰子默认为6个面."""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数之间的随机值."""
        return randint(1, self.num_sides)   #方法roll()使用函数randint()来返回一个1和面数之间的随机数
# 方法-init_()接受一个可选参数。
# 创建这个类的实例时,如果没有指定任何实参，面数默认为6;如果指定了实参,这个值将用于设置股子的面数(见0)。
# 股子是根据面数命名的,6面 的股子名为D6, 8面的股子名为D8,依此类推。
# 方法roll()使用函数randint()来返回一个1和面数之间的随机数(见0)。这个函数可能返回起始值1、终止值num_sides或这两个值之间的任何整数。
