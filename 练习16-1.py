# 锡特卡的降雨量
# 锡特卡属于温带雨林，降水量非常丰富。在数据文件sitka_weather_2018_simple.csv 中，
# 文件头PRCP表示的是每日降水量，请对这列数据进行可视化。如果你想知道沙漠的降水量有多低，可针对死亡谷完成这个练习。
import csv学习
from datetime import datetime
from matplotlib import pyplot as plt
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
# 从文件中获取日期和降雨量。
    dates, precips = [], []            #precips：降水
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        precip = float(row[3])
        precips.append(precip)
# 绘制降雨量图形。
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, precips, c='blue')
# 设置图形的格式。
plt.title("Daily Rainfall Amounts - 2018", fontsize=24)
plt.xlabel('日期', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

