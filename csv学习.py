import csv

header = ['number', 'name', 'gender', 'math', 'score']
rows = [[1, 'xiaoming', 'male', 88, 67],
        [2, 'xiaohong', 'female', 95, 89],
        [3, 'xiaozhang', 'female', 67, 50],
        [4, 'xiaoli', 'male', 99, 92]]

with open('test.csv', 'w') as f:
    w = csv.writer(f)
    print(w)
    print(type(w))
    w.writerow(header)
    w.writerow(rows)




import csv学习

with open('test1.csv', 'w') as f1:
    w1 = csv.DictWriter(f1, fieldnames=['number', 'name', 'gender', 'math', 'score'])
    w1.writeheader()
    w1.writerows = ({1, 'xiaoming', 'male', 88, 67},
                    {2, 'xiaohong', 'female', 95, 89},
                    {3, 'xiaozhang', 'female', 67, 50},
                    {4, 'xiaoli', 'male', 99, 92},
                    {1, 'xiaoming', 'male', 88, 67},
                    {2, 'xiaohong', 'female', 95, 89},
                    {3, 'xiaozhang', 'female', 67, 50})

# : 4,'xiaoli','male',99,92]]
#
#
#
#
# #Week9_Python_in_AI
#
#       w1.writerow


# 'number': 1, 'name': 'xiaoming', 'gender': 'male', 'math': 88, 'score': 67})
#    w1.writerow{['number': 2, 'name': 'xiaohong', 'gender': 'female', 'math': 95, 'score': 89
#    w1.writerow[['number': 3, 'name': 'xiaozhang', 'gender': 'female', 'math': 67, 'score': 5
#    w1.writerow[['number': 4, 'name': 'xiaoli', 'gender': 'male', 'math': 99, 'score': 92})
#    w1.writerow[['number': 1, 'name': 'xiaoming', 'gender': 'male', 'math': 88, 'score': 67})
#    w1.writerow[['number': 2, 'name': 'xiaohong', 'gender': 'female', 'math': 95, 'score': 89
#    w1.writerow[['number': 3, 'name': 'xiaozhang', 'gender': 'female', 'math': 67, 'score': 5
#    w1.writerow[['number': 4, 'name': 'xiaoli', 'gender': 'male', 'math': 99, 'score': 92})
