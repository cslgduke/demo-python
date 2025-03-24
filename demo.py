from __future__ import print_function  # from __future__ imports must occur at the beginning of the file
import sys
import time
import calendar
from support import sum_func
import math


print("Hello world")
list = ["a", "b", "c"]
print(list)

if True:
    print("True")
else:
    print("False")

if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    # unindent does not match any outer indentation level
    # python doesn't use braces to identify block,instead, all the  adjacent code lines with the same indentation will be seen as a block,  so has a strict requirements for indent
    print("False")

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days)

name = "Runoob"
print(name)

# raw_input("press enter to exit, otherwise display what you print...\n")

x = 'runoob';
sys.stdout.write(x + '\n')

print(x, '\t*****', name)

str = 'Hello World!'
print(str[0:5])
print("***************List******************")
list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)
print(list[1:2])
print(tinylist * 2)  # 输出列表两次
print(list + tinylist)  # 打印组合的列表

print("***************Dictionary******************")
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'runoob', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # 输出键为'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

print("***************Date and Time******************")
ticks = time.time()
print("current timestamp is:", ticks);

localtime = time.localtime(time.time())
print("localtime is:", localtime)
print("year of localtime is:", localtime[0])
print("month of localtime is:", localtime[1])

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print("***************Calendar******************")
cal = calendar.month(2024, 7)
print(cal)

print("***************function******************")


def printme(str):
    "print your parameters"
    print(str)
    return


printme("Hello Python function")


def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("Name: ", name)
    print("Age ", age)
    return


printinfo(age=50, name="miki")
printinfo(name="miki")

print("***************lambda******************")
sum = lambda arg1, arg2: arg1 + arg2
print("The added value is: ", sum(10, 20))
print("The added value is: ", sum(20, 20))

print("***************module******************")
# import support
# print(support.sum_func(10, 20, 30))
print(sum_func(10, 20, 30))

print("***************dir()******************")
content = dir(math)
print(content)

from demo_obj import Employee
emp = Employee("Zara", 2000)
emp.displayEmployee()
