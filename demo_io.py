# str = input("Please input your text(press Enter to end):")
# print ("You input content is: ", str)

import os

fo = open("foo.txt", "w")
fo.write("www.runoob.com!\nVery good site!\n")

# 关闭打开的文件
fo.close()

fo = open("foo.txt", "r+")
# str = fo.read(10)
str = fo.read()
print("read content is: ", str)
# 关闭打开的文件
fo.close()

fo = open("foo.txt", "r+")
str = fo.read(10)
print("read content is: ", str)
position = fo.tell()
print("current position is: ", position)

fo.seek(0, 0)
str = fo.read()
print("read content is: ", str)
position = fo.tell()
print("current position is: ", position)

fo.close()

os.rename("foo.txt","foo-2.txt")
print(os.getcwd())