# 练习16-4 本节以硬编码的方式指定了TMIN和TMAX列的索引。
# 请根据文件头行确定这些列的索引，让程序能够同时适用于锡特卡和死亡谷。另外，根据气象站的名称自动生成图表的标题。
# 方法index()返回列表中特定元素的索引，如下面的代码所示：
import csv学习
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
filename = 'data/sitka_weather_2018_simple.csv'
place_name = ''
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    date_index = header_row.index('DATE')
    high_index = header_row.index('TMAX')
    low_index = header_row.index('TMIN')
    name_index = header_row.index('NAME')
    # 从文件中获取日期、最高气温和最低气温。
    dates, highs, lows = [], [], []
    for row in reader:
        # 如果没有设置气象站的名称，就获取它。
        if not place_name:
            place_name = row[name_index]
            print(place_name)
            current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
# 绘制显示最高气温和最低气温的图形。
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 设置图形的格式。
title = f"Daily high and low temperatures - 2018\n{place_name}"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
