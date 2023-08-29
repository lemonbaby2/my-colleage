# 1. python中创建新的csv文件   编译文件先关闭excel
# (1). 使用csv.writer()创建：
import csv学习

headers = ['学号', '姓名', '分数']
rows = [('202001', '张三', '98'),
        ('202002', '李四', '95'),
        ('202003', '王五', '92')]
with open('score.csv', 'w', encoding='GB2312', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

