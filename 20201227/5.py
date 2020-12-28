'''
5.数组list1和list2为随机生成的数组，输出他们中间相同的数的和，如果没有相同的数则输出两个数组无相同数字。
'''
import random
list1 = []
s = random.randint(1,20)
for i in range(0,s):
    list1.append(random.randint(0,100))
list2 = []
for i in range(0,s):
    list2.append(random.randrange(0,100))
a = set(list1) & set(list2)
print(sum(a))
if sum(a) == 0:
    print("两个数组无相同数字！")