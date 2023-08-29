import csv#学习

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

# 16.1.2打印文件头及其位置
import csv学习

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index_header, column_header in enumerate(header_row):  # enumerate :枚举法
        print(index_header, column_header)

# 16.1.3 提取并读取数据
import csv学习

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件中获取最高温度。
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# 创建一个名为highs的空列表(见0),再遍历文件中余下的各行(见0)。
# 阅读器对象从其 停留的地方继续往下读取CSV文件,每次都自动返回当前所处位置的下一行。
# 由于已经读取了 文件头行,这个循环将从第二行开始-从这行开始包含的是实际数据。
# 每次执行循环时,都将 索引5处(TMAX列)的数据附加到highs末尾(见0)。
# 在文件中,这项数据是以字符串格式存 储的,因此在附加到highs末尾前,使用函数int()将其转换为数值格式,以便使用。


# 16.1.4 绘制温度图表
import csv学习

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件中获取最高温度。
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

    # 根据最高温度绘制图形。
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(highs, c='pink')

# 设置图形的格式。
ax.set_title("2018年7月每日最高温度", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("温度 （F）", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'  # 可能是因为matplotlib的默认字体不支持中文，然后要手动地调为另一种字体.
plt.rcParams['axes.unicode_minus'] = False
plt.show()

# 16.1.6 在图表中添加日期
# 首先导入模块datetime中的datetime类，再调用方法strptime(),并将包含所需日期的字符串作为第一个实参。
# 第二个实参告诉py如何设置日期格式,方法strptime()可接受各种实参。
# 通过提取日期和最高温度并将其传递给plot（），对温度进行改进
import csv学习
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# 从文件中获取日期和最高温度。
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# 根据最高温度绘制图形。
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# 设置图形的格式。
ax.set_title("2018年7月每日最高温度", fontsize=24) # 先自己找出错误
ax.set_xlabel('日期 （天）', fontsize=16)
fig.autofmt_xdate()    # 调用fig.autofmt_xdate()来绘制倾斜的日期标签，以免其彼此重叠。
ax.set_ylabel("温度 （F）", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'  # 可能是因为matplotlib的默认字体不支持中文，然后要手动地调为另一种字体.
plt.rcParams['axes.unicode_minus'] = False
plt.show()


# 16.1.7涵盖更长的时间。
import csv学习
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# 从文件中获取日期和最高温度。
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# 根据最高温度绘制图形。
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# 设置图形的格式。
ax.set_title("2018年每日最高温度", fontsize=24) # 先自己找出错误
ax.set_xlabel('日期 （天）', fontsize=16)
fig.autofmt_xdate()        #   调用fig.autofmt_xdate()来绘制倾斜的日期标签，以免其彼此重叠。
ax.set_ylabel("温度 （F）", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'  # 可能是因为matplotlib的默认字体不支持中文，然后要手动地调为另一种字体.
plt.rcParams['axes.unicode_minus'] = False
plt.show()




print(plt.style.available)
