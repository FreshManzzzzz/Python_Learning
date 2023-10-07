# 练习一 条件语句的使用
# 1. 使用if语句判断字符串的长度是否等于10，根据判断结果进行不同的输出
str1 = input("Please input a string:")
if len(str1) < 10:
    print("字符串长度小于10")
elif len(str1) == 10:
    print("字符串长度等于10")
else:
    print("字符串长度大于10")

# 2. 提示用户输入一个1-40之间的数字，使用if语句根据输入数字的大小进行判断，如果输入的数字在 1-10，11-20，21-30，31-40，分别进行不同的输出
num = input("Please input a number(1-40):")
if int(num) <= 10:
    print("大于1小于等于10")
elif int(num) <=20:
    print("大于10小于等于20")
elif int(num) <= 30 :
    print(("大于20小于等于30"))
else:
    print("大于30小于等于40")
