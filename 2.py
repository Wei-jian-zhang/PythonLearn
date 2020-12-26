'''
2.有已知数组alist,数组blist，请输出两个数组中，不相同的数的值的和。
'''
list = []
alist = [15,20,17,19,135,443,500,900]
blist = [71,35,49,15,114,533,557,1546]
c = set(alist) ^ set(blist)
print(sum(c))