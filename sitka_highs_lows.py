# 16.1.8再绘制一个数据系列\
import csv学习
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# 从文件中获取日期和最高温度。
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
# 根据最高温度绘制图形。
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='green')
# 设置图形的格式。
ax.set_title("2018年每日最高温度", fontsize=24) # 先自己找出错误
ax.set_xlabel('日期 （天）', fontsize=16)
fig.autofmt_xdate()        #   调用fig.autofmt_xdate()来绘制倾斜的日期标签，以免其彼此重叠。
ax.set_ylabel("温度 （F）", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)


plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'  # 可能是因为matplotlib的默认字体不支持中文，然后要手动地调为另一种字体.
plt.rcParams['axes.unicode_minus'] = False
plt.show()


# 16.1.9绘图区域着色
import csv学习
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# 从文件中获取日期和最高温度。
    dates, highs, lows = [], [],[]
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)
# 根据最高温度绘制图形。
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='green', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.ylim(10, 130)
#添加两个数据系列后,就可以知道每天的温度范围了。下面来给这个图表做最后的修饰，通过着色来呈现每天的温度范围。
# 为此,将使用方法fill_between()。它接受一个x值系列和两个 y值系列,并填充两个y值系列之间的空间.

# 1处的实参alpha指定颜色的透明度。alpha值为0表示完全透明,为1(默认设置)表示完全不透明。
# 通过将alpha设置为0.5,可让红色和蓝色折线的颜色看起来更浅。
# 在1处,向fill_between()传递一个x值系列(列表dates),以及两个y值系列(highs和 lows)。
# 实参facecolor指定填充区域的颜色,还将alpha设置成了较小的值0.1,让填充区域将两个数据系列连接起来的同时不分散观察者的注意力。
# 显示了最高温度和最低温度之间的区域被填充后的图表。



# 设置图形的格式。
ax.set_title("2018年每日最高温度", fontsize=24) # 先自己找出错误
ax.set_xlabel('日期 （天）', fontsize=16)
fig.autofmt_xdate()        #   调用fig.autofmt_xdate()来绘制倾斜的日期标签，以免其彼此重叠。
ax.set_ylabel("温度 （F）", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)


plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'  # 可能是因为matplotlib的默认字体不支持中文，然后要手动地调为另一种字体.
plt.rcParams['axes.unicode_minus'] = False
plt.show()



