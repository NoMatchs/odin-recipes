# # # # import numpy as np
# # # # a = np.arange(24).reshape(2, 3, 4)
# # # # print(a.ndim)
# # # # print(a.shape)
# # # # print(a.size)


# # # # import numpy as np


# # # # sum = 0
# # # # i = 1
# # # # while i <= 1000:
# # # #     sum += i
# # # #     i += 1
# # # # print("sum =",sum)

# # # # sum = 0
# # # # for i in range(1,21):
# # # #     if i % 3 == 0:
# # # #         sum += i
# # # # print(sum)

# # # # for i in range(1,6):
# # # #     for j in range(i):
# # # #         print("*", end=" ")
# # # #     print()

# # # # for i in range(1,5):
# # # #     for j in range(1,5):
# # # #         if i == j:
# # # #             print(1,end = " ")
# # # #         else:
# # # #             print(0,end = " ")
# # # #     print()



# # # for i in range(4):
# # #     for j in range(4):
# # #         if i == j:
# # #             print(1,end=" ")
# # #         else:
# # #             print(0,end=" ")
# # #     print()



# # # for i in range(6):
# # #     for j in range(i):
# # #         print("*",end = " ")
# # #     print()

# # # peach = 1
# # # for day in range(4,0,-1):
# # #     peach = (peach + 1) * 2
# # # print(peach)

# # # peach = 1
# # # for day in range (4,0,-1):
# # #     peach = (peach + 1) * 2
# # #     print("第",day,"天的桃子数为：",peach)

# # # for gj in range(51):
# # #     for mj in range(34):
# # #         xj = 100 - gj - mj
# # #         if(2 * gj + 3 * mj + 0.5 * xj == 100):
# # #             print("gj:",gj," mj:",mj," xj:",xj)


# # list_search = [2,6,13,25,38,37,41,58,69]

# # target = 25

# # left, right = 0, len(list_search) - 1

# # found = False

# # while left <= right:
# #     mid = (left + right) // 2
# #     if list_search[mid] == target:
# #         found = True
# #         break
# #     elif list_search[mid] < target:
# #         left = mid + 1
# #     else:
# #         right = mid - 1

# # if found == True:
# #     print("25在列表中")
# # else:
# #     print("25不在列表中")

# list_search = [2,6,13,25,33,37,41,58,69]
# target = 33

# left, right = 0, len(list_search)
# found = False

# while left <= right:
#     mid = (left + right) // 2
#     if list_search[mid] == target:
#         found = True
#         break
#     elif list_search[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# if found:
#     print("It is Exist")
# else:
#     print("It isn't Exist")

# list1 = [8,3,1,5,2]
# n = len(list1)

# for i in range(n-1):
#     for j in range(n-1-i):
#         if list1[j] > list1[j+1]:
#             list1[j],list1[j+1] = list1[j+1],list1[j]
# print(list1)

# def fib(n):
#     if n <= 1:
#         return n
#     return fib(n-1) + fib(n-2)

# total = 0
# for i in range(20):
#     total += fib(i)
# print(total)

# for i in range(10):
#     print(i)

# import math

# sin_45 = math.sin(math.pi/4)

# e_squared = math.e**2

# log_10 = math.log10(80)

# sqrt_18 = math.sqrt(18)

# result = sin_45 + (e_squared + log_10) / sqrt_18

# print(result)

# print("%.2f"%13.345)

# sum = 0
# i = 1

# while i <= 100:
#     sum += i
#     i += 1

# print("sum is", sum)

# sum = 0
# for i in range(21):
#     if(i % 3 == 0):
#         print(i)
#         sum += i
# print("sum is", sum)

# for i in range(1,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# for i in range(5):
#     print(i)

# for j in range(0,5):
#     print(j)

# for i in range(4):
#     for j in range(4):
#         if i == j:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()


# total = 1;
# for i in range(4,0,-1):
#     total = (total + 1) * 2
# print("total is",total)

# for gj in range(51):
#     for mj in range(34):
#         xj = 100 - gj - mj
#         if(xj * 0.5 + gj * 2 + mj * 3 == 100):
#             print("gj is",gj, "  mj is",mj,"  xj is",xj)

# list_search = [2,6,13,25,28,37,41,58,69]

# target = 25

# left,right = 0,len(list_search)
# found = False

# while left <= right:
#     mid = (left + right) // 2
#     if list_search[mid] == target:
#         found = True
#         break
#     elif list_search[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# if found:
#     print("找到了")
# else:
#     print("没找到")


# list1 = [8,3,1,5,2]
# n = len(list1)

# for i in range(n-1):
#     for j in range(n - 1 - i):
#         if list1[j] > list1[j + 1]:
#             list1[j],list1[j + 1 ] = list1[j + 1],list1[j]
# print("排序后：",list1)

# import random
# # 字符集合.
# str01 = "0123456789abcdefghijklmnopqrstuvwxyaABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # 生成验证码
# # -----begin-------
# yzm = ''.join(random.sample(str01,4))
# # -----end---------
# print("当前验证码:", yzm)
# # 验证码验证
# yzmInput = input("请输入验证码: ")
# if yzm == yzmInput:  # 验证码验证.
#     print("验证通过！")
# else:
#     print("验证失败！")

# import abc

# # 定义抽象类.
# class People:
#     # -----begin-------
#     @abc.abstractmethod
#     def working(self):
#         pass
#     # -----end---------

# # 定义抽象类People的派生类.
# class Chinese(People):
#     # 实现抽象类的抽象方法working().
#     def working(self):
#         print("中国人都在勤奋地工作...")

# # 创建Chinese类的对象.
# c1 = Chinese()
# c1.working()

# c2 = Chinese()
# c2.working()
# import math

# sin_45 = math.sin(math.pi/4)

# e_squared = math.e**2

# log_10 = math.log10(80)

# sqrt_18 = math.sqrt(18)

# result = sin_45 + (e_squared + log_10) / sqrt_18

# print(result)

# import math

# sin_45 = math.sin(math.pi/4)

# e_2 = math.e**2

# log_10_88 = math.log10(80)

# sqrt_18 = math.sqrt(18)

# print(sin_45 + (e_2  +log_10_88) / sqrt_18)

# sum = 0
# i = 1

# while i <= 100:
#     sum += i
#     i += 1
# print("1-100的和：",sum)

# print()

# sum = 0
# for i in range(1,21):
#     if i % 3 == 0:
#         sum += i
# print("1-20能被3整出的所有数的和：",sum)

# print()

# for i in range(6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# print()

# for i in range(4):
#     for j in range(4):
#         if i == j:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()

# print()

# total = 1
# for i in range(4,0,-1):
#     total = (total + 1) * 2
# print("猴子一开始摘了桃子数是：",total)

# print()

# for gj in range(51):
#     for mj in range(34):
#         xj = 100 - gj -mj
#         if(xj * 0.5 + mj * 3 + gj * 2 == 100):
#             print("公鸡数：",gj," 母鸡数：",mj," 小鸡数：",xj)
# print()

# list_search = [2, 6, 13, 25, 28, 37, 41, 58, 69]

# left, right = 0,len(list_search)
# target = int(input("你想查找的数字>:"))

# Is_found = False

# while left <= right:
#     mid = (left + right) // 2
#     if list_search[mid] == target:
#         Is_found = True
#         break   
#     elif list_search[mid] < target:
#         left = mid + 1
#     else:
#         right = mid - 1

# if Is_found:
#     print("你查找的数字",target,"是存在的")
# else:
#     print("不存在")

# print()

# list1 = [8, 3, 1, 5, 2]

# n = len(list1)

# for i in range(n - 1):
#     for j in range(n - 1 - i):
#         if list1[j] < list1[j+1]:
#             list1[j],list1[j+1] = list1[j+1],list1[j]
# print("排序后：",list1)

# print()

# def fib(n):
#     if n <=1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)

# sum = 0
# for i in range(20):
#     sum += fib(i)
# print("斐波那契前20项之和：",sum)

# print(1 + 1)
# print(1 * 1)
# print(3 / 2)
# print(3 // 2)
# print(1 - 1)

# a = 1 #赋值
# b = 3
# print(a + b)

# if a == b: #等于=
#     print(a + b)
# else:
#     print(a - b)

# Calculator = input("请输入你想要的运算符号>")
# operator = ""

# if Calculator == "+": 
#     operator = "Plus" #字符串
# elif Calculator == "-":  # else if
#     operator = "Subtraction"
# elif Calculator == "/":
#     operator = "Division"
# elif Calculator == "*":
#     operator = "Multiplication"

# digital_1 = int(input("第一个数>"))
# digital_2 = int(input("第二个数>"))

# result = 0

# if operator == "Plus":
#     result = digital_1 + digital_2
# if operator == "Subraction":
#     result = digital_1 - digital_2
# if operator == "Multiplication":
#     result = digital_1 * digital_2
# if operator == "Division":
#     result = digital_1 / digital_2

# print("运行结果：",result)

# a = 1
# b = 1

# while a == b: # while 条件
#     result = a + b # 2 
#     print(result)
#     if a == b:
#        a = a + 1 # a += 1
#     if a != b:
#         break

# a,b = map(int,input().split())

# Calculator = a + b

# print(Calculator)


# Sum = 0

# k = int(input()) # 1
# n = 0

# while k >= Sum:
#     n += 1
#     Sum += 1 / n # Sum += 1 / n
    

# print(n)

# import pandas as pd
# import seaborn as sns

# # 直接从 seaborn 加载泰坦尼克数据集
# titanic = sns.load_dataset('titanic')
# print(titanic.head())

# array = [5,4,3,2,1]

# for i in range(5): #for循环 范围[0,5) 0 1 2 3 4 增大
#     for j in range(5):
#         print(i + j)
    

# print("退出循环了")

# a = 16.8
# b = 16.8

# print(id(a))
# print(id(b))

# print(id(a) == id(b))

# i = 0
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1;
# print("sum",sum)


# sum = 0
# for i in range(1,21):
#     if i % 3 == 0:
#         sum += i
# print("sum =",sum)

# for i in range(5):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(4):
#     for j in range (4):
#         if i == j:
#             print("1",end=" ")
#         else:
#             print("0",end=" ")
#     print()


# total = 0
# for i in range(5,0,-1):
#     total = (total + 1) * 2
# print(total)

# for gj in range(51):
#     for mj in range(34):
#         xj = 100 - mj - gj
#         if xj * 0.5 + gj * 2 + mj * 3 == 100:
#             print("公鸡数：",gj,"母鸡数：",mj,"小鸡数:",xj)

# import random
# # 字符集合.
# str01 = "0123456789abcdefghijklmnopqrstuvwxyaABCDEFGHIJKLMNOPQRSTUVWXYZ"
# # 生成验证码
# # -----begin-------
# yzm = "".join(random.sample(str01,4))
# # -----end---------
# print("当前验证码:", yzm)
# # 验证码验证
# yzmInput = input("请输入验证码: ")
# if yzm == yzmInput:  # 验证码验证.
#     print("验证通过！")
# else:
#     print("验证失败！")

# import abc

# # 定义抽象类.
# class People:
#     # -----begin-------
#     @abc.abstractmethod
#     def working(self):
#         pass
#     # -----end---------

# # 定义抽象类People的派生类.
# class Chinese(People):
#     # 实现抽象类的抽象方法working().
#     def working(self):
#         print("中国人都在勤奋地工作...")

# # 创建Chinese类的对象.
# c1 = Chinese()
# c1.working()

# import math

# sin_45 = math.sin(math.pi / 4) 

# e_2 = math.e ** 2

# log_10_80 = math.log10(80)

# Sqrt_18 = math.sqrt(18)

# print(sin_45 + (e_2 + log_10_80) / Sqrt_18)


# import random

# list1 = [random.randint(1,100) for _ in range(10)]
# print("原始列表：",list1)

# list2 = []

# for num in list1:
#     if num % 2 == 1:
#         list2.append(num ** 2)
#     else:
#         list2.append(num ** 3)
# print("变换后列表:",list2)

# import random

# l1 = [random.randint(1,100) for _ in range(10)]
# print("原始类表：",l1)

# l2 = []

# for num in l1:
#     if num % 2 == 1:
#         l2.append(num ** 2)
#     else:
#         l2.append(num ** 3)
# print("交换后：",l2)
# def func(n):
#     if n % 2 == 0:
#         total = sum(1 / i for i in range(2,2*n + 1,2))
#     else:
#         total = sum(1 / i for i in range(1,2*n + 2,2))
#     return total
# print(func(2))
# print(func(3))
# print(func(4))


# def func(n):
#     if n % 2 == 0:
#         total = sum(1 / i for i in range(2, 2 * n + 2,2))
#     else:
#         total = sum(1 / i for i in range(1,2 * n + 1,2))
#     return total

# print(func(2))
# print(func(3))
# print(func(4))

# import random

# l1 = (random.randint(1,100) for _ in range(10))

# l2 = []

# for i in l1:
#     if i % 2 == 1:
#         l2.append(i ** 2)
#     else:
#         l2.append(i ** 3)
# print(l2)

# list_search = [2, 6, 13, 25, 28, 37, 41, 58, 69]

# left,right = 0,len(list_search) - 1

# target = 25

# Find = False

# while left <= right:
#     mid = (left + right) // 2
#     if list_search[mid] == target:
#         Find = True
#         break
#     elif list_search[mid] > target:
#         right = mid - 1
#     else:
#         left = mid + 1
# if Find == True:
#     print("找到啦")
# else:
#     print("没找到")


list1 = [8, 3, 1, 5, 2]

n = len(list1)

for i in range(n -1):
    for j in range(n - i - 1):
        if list1[j] > list1[j + 1]:
           list1[j],list1[j + 1] = list1[j + 1],list1[j]

print(list1)

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

sum = 0

for i in range(1,21):
    sum += fib(i)
print(sum)