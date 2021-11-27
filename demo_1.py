# -*- coding = utf-8 -*-
# @Time: 2021/11/27 19:16
# @Author: 宋林凯
# @File: demo_1.py
# @Software: PyCharm
import  keyword
print(keyword.kwlist)
print("------------------------------------")

# 区别两种写法
a = 18
print("小明的年龄是%d"%a)
print("小明的年龄是%d",a)
print("------------------------------------")

# 输出字符串和数字
b = 20
print("我的名字叫%s,国籍是%s"%('小宋','中国'))
print("我年龄是%d"%b)
print("------------------------------------")

print('aaa','bbb','ccc') # 自动有空格
print('www','baidu','com',sep = '.') # sep自动连接三个独立部分
print('hello',end = '')
print('world',end = '\t')
print('python',end = '\n')
print('end')
print("------------------------------------")

password = input('请输入密码:')  # 输入的都是字符串
print('请输入你的密码是：',password)
print("------------------------------------")

# 打印类型
c = 10
print(type(c))

# 字符串变成整型
a = int("123")
print(type(a))