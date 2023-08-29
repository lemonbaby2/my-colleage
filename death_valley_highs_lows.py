# 16.1.10 错误检查
import csv

from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件中获取日期和最高温度。
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
# 根据最高温度绘制图形。
plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='green', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 设置图形的格式。
ax.set_title("2018年每日最高温度和最低温度\n美国加利福尼亚州死亡谷", fontsize=24)  # 先自己找出错误
ax.set_xlabel('日期 （天）', fontsize=16)
fig.autofmt_xdate()  # 调用fig.autofmt_xdate()来绘制倾斜的日期标签，以免其彼此重叠。
ax.set_ylabel("温度 （F）", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.rcParams['font.sans-serif'] = 'Microsoft YaHei'  # 可能是因为matplotlib的默认字体不支持中文，然后要手动地调为另一种字体.
plt.rcParams['axes.unicode_minus'] = False
plt.show()

# 使用的很多数据集都可能缺失数据，格式不正确或数据本身不正确。在这里，使用了一个try——except——else代码块处理数据缺失问题。
# 在有些情况下，需要使用continue来跳过一些数据，或者使用remove（）或del将已提取的数据删除。

# 16.1.11自己动手下载数据
