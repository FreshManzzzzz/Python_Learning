# 练习三 列表的基本操作
# 1. 定义一个含有5个数字的列表
# 2. 为列表增加一个元素 100
# 3. 使用remove()删除一个元素后观察列表的变化
# 4. 使用切片操作分别取出列表的前三个元素，取出列表的最后一个元素

list1 = [1,2,3,4,5]
list1.append(100)
print(list1)
list1.remove(1)
print(list1)
print(list1[0:3])
print(list1[-1])