"""
输入三个整数x,y,z，请把这三个数由小到大输出。

"""

list = []
x = int(input("输入一个整数："))
y = int(input("请输入一个整数："))
z = int(input("请输入一个整数："))
list.append(x)
list.append(y)
list.append(z)
list.sort()
print(list)

"""
"""
for i in range(1, 10):
    print()
    for j in range(1, i + 1):
        print("%d*%d=%d" % (i, j, i * j), end=" \t")

"""
题目：暂停一秒输出。

程序分析：使用 time 模块的 sleep() 函数。
"""
import time

l = [1, 2, 3, 4]
for i in range(len(l)):
    print(l[i])
    time.sleep(1)  # 暂停一秒输出

"""
题目：判断101-200之间有多少个素数，并输出所有素数。

程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
"""
i = []
for a in range(101, 201):
    for b in range(2, a):
        if a % b == 0:
            break
    else:
        i.append(a)
print(i)
print(len(i))

"""
题目：判断101-200之间有多少个素数，并输出所有素数。

程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
"""
i = []
for a in range(101, 201):
    for b in range(2, a):
        if a % b == 0:
            break
    else:
        i.append(a)
print(i)
print(len(i))
