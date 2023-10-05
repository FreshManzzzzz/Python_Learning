# 练习四 元组的基本操作
# 1. 定义一个任意元组，对元组使用append() 查看错误信息
# 2. 访问元组中的倒数第二个元素
# 3. 定义一个新的元组，和 1. 的元组连接成一个新的元组
# 4. 计算元组元素个数
tup1 = (1,2,3,4,5,6)
# tup1.append(7)  #'tuple' object has no attribute 'append'
print(tup1[-2])
tup2 = (4,5,6)
tup3 = tup1 + tup2
print(tup3)
print(len(tup3))
print(tup3.__len__())
