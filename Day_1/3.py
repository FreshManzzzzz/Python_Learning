# 练习二 字符串基本操作
# 1. 定义两个字符串分别为 xyz 、abc
# 2. 对两个字符串进行连接
# 3. 取出xyz字符串的第二个和第三个元素
# 4. 对abc输出10次
# 5. 判断a字符（串）在 xyz 和 abc 两个字符串中是否存在，并进行输出

str1 = 'xyz'
str2 = 'abc'
str3 = str1 + str2
print(str3)
print(str1[1],str1[2])
print(str2 * 10)
print('a' in str1)
print('a' in str2)
