"""
1.数字a从0开始每次递增1，数字b从1开始每次递增2，数字C从2开始每次递增3，求：当三个数字递增到200时，a b c有几次相等。
"""
list = []
for a in range(0,201,1):

    for b in range(1,201,2):

        for c in range(2,201,3):
            if a == b ==c:
                list.append(a)
print(len(list))