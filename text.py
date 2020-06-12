# print("Python","输出","可以","分段")

# 缩进的方式 ：
# a=100
# if a>=0:
#     print(a)
# else:
#     print(-a)

# 数据类型
# print('测试整数：',100,'\n','测试浮点数：',1.23e-2,'\n','测试字符串：','I\'m \"张三\"')

# 字符串类型的换行和不转义的其他表现形式 r'' ,'''...
# print(r'I am \n ok')
# print('''这是第一行
# ....这是第二行
# ...这是第三行
# ...这是第四行''')

# 布尔值的 and or not 运算
# print(True and False)
# print(True or False)
# print(not True)


# name = 0
# if name is None:
#     print("这是个空值None")
# else:
#     print("这不是一个空值")


# 动态变量
# a = 3
# print(a)
#
# a = 'xzy'
# print(a)

# PI = 3.14   常量和除法的一些种类
# print(PI)
# PI = 3.1415
# print(PI)
#
# print(10/3)
# print(10//3)
# print(10%3)

# 单个字符的编码和字符转换函数
# print(ord('S'))
# print(chr(89))

# 编码指定方式
# print('中文'.encode('utf-8'))
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 字符长度计算函数
# print(len('中文'))
# print(len(b'\xe4\xb8\xad\xe6\x96\x87'))

# 输出格式化字符串
# print('输出的是一个整数：%d，还有一个字符串：%s %%' % (2, '张三'))

# list列表的增删改
# animal = ['dog', 'cat', 'tiger', 34, ['fly', 'run'], 'people']
# print(animal)
# print(animal[1])
# print(animal[-1])
#
# # list末尾增加元素 .append()
# animal.append('man')
# print(animal[-1])
#
# # 指定位置插入元素
# animal.insert(1, 'bee')
# print(animal)
#
# # 删除元素
# animal.pop(0)
# print(animal)

# tuple

# ani = ('ab', 'cd', 'ef', 'gh', ['a', 'b'])
# print(ani)
# ani[4][0] = 'x'
# ani[4][1] = 'y'
#
# print(ani)


# 条件判断 elif 就是else if 的缩写 input（括号的内容） int（）强制类型转换

# a = int(input('输入一个数字：'))  #input()返回的是str 需要进行类型转换
#
# if a > 4:
#     print("大于4")
# elif a == 4:
#     print("等于4")
#
# elif a < 4:
#     print("小于4")
# else:
#     print("输入有误")

# 条件练习 input()的返回类型 round()函数

# tz = int(input('请输入体重：'))
# sg = float(input("请输入身高："))
# bmi = round(tz / (sg * sg), 1)
#
# if bmi < 18.5:
#     print("过轻")
# elif (bmi >= 18.5 and bmi <= 25):
#     print("正常")
# elif bmi >=25 and bmi <= 28:
#     print("过重")
# elif (bmi >= 28 and bmi <= 32):
#     print("肥胖")
# else:
#     print("严重肥胖")

# for x in xs 循环方式

# sum = 0
# # for x in list(range(101)):
#     sum = sum + x
# print(sum)

# while 循环方式

# l = ['张三', '李四', '王五']
# i = len(l) - 1
# while i >= 0:
#     print("hello,%s" % l[i])
#     i = i-1

# 跳出循环的方式 break continue

# for x in list(range(11)):
#     if x == 6:
#         continue
#     print(x)

# dict 字典的使用

# noname = {'a': 34, 'b': 35, 'c': 90}
# print(noname['a'])
#
# # 判断 dict key值是否存在的两种方式
# print('c' in noname)
# print('d' in noname)
#
# print(noname.get('c', -1))
# print(noname.get('d', -1))

# set的用法 :利用list赋值，不包括重复值

# s = set([1, 2, 3, 3, 4])
# print(s)
# # add(key)
# s.add(5)
# print(s)
# # remove(key)
# s.remove(1)
# print(s)


# str不可变对象和可变对象的区别
# s = 'abc'
# s.replace('a', 'A')
# print(s)
#
# l = ['b', 'a', 'c']
# l.sort()
# print(l)

# 函数的问题 数据类型转换
# a = int('2') #字符内必须是整数
# b = str(24)
# c = bool(1)
# d = bool('')
# e = hex(3)
# print(a, b, c, d,e)

# 定义函数 ,
# def my_abs(x):
#
#     if x < 0:
#         return -x
#     else:
#         return x
# print(my_abs(-19), my_abs(19))

# 空函数，参数检查 和 抛出异常
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError("This a TypeError!")
#     if x < 0:
#         return -x
#     elif x == -10:
#         pass
#     else:
#         return x
#
# print(my_abs(-19), my_abs(19), my_abs(-10))

# 返回多个值,并且引用了一个包
# import math
#
# def csd(x, y):
#     nx = x*math.cos(60)
#     ny = y*math.sin(60)
#     return nx, ny
#
# a, b= csd(3,4)
# print(a,b)

# import math
# def quadratic(a, b, c):
#     if not isinstance(a,int):
#         raise TypeError("not int!")
#     if not isinstance(b, int):
#         raise TypeError("not int!")
#     if not isinstance(c, int):
#         raise TypeError("not int!")
#     if (b*b - 4*a*c) >= 0:
#         x = (-b + math.sqrt(b * b - 4 * a * c)) / 2 * a
#         y = (-b - math.sqrt(b * b - 4 * a * c)) / 2 * a
#     else:
#         return
#     return x,y
#
# print(quadratic(1,-2,4))

# 函数的参数问题
# 默认参数

# def per(name, age, add='beijing'):
#     print(name, age, add)
#
# per("bob", 3)
# per('cid',6,'shangh')

# 可变对象不能作为默认参数
# def add(l=[]):
#     l.append("end")
#     return l
# print(add([]),add())

# 可变参数：相当于去掉括号的list或者tuple

# def power(*numbers):
#     sum = 0
#     for x in numbers:
#         sum = sum +x
#
#     return sum
# print(power(1,2,3,4))
# print(power(1,2,3))
# a = [1,2,3,4,5]
# print(power(*a))

# 关键字参数：相当于去掉括号的dict

# def person(name,age,**other):
#     print("name=", name, "age=", age, "other", other)
# person('zhang', 25)
# person('li',12, city= 'biejing')
# person('li',12, city= 'biejing',home ='lij')
#
# fair = {'add' :'SSS','qq':8055}
# person('li',12, **fair)

# 命名关键字参数 *， 之后是指定的关键字名字
#                *name,可变参数之后，不用加*

# def people(name, age, *, city, add):
#     print(name, age,city,add)
# def person(name, age, *l, city,add):
#     print(name, age, l, city, add)
#
# people('li',3,city = 'shagnhai' ,add = 'sf')
# person('zhang',4,'d','f',city='sdfs',add = 'fs')

# 递归函数
# def power(n):
#     if n == 1:
#         return 1
#     return n * power(n-1)
# print(power(5))

# 高级特性：切片：取list或tuple中的部分值,字符串也可以
# l = [1, 2, 3, 4, 5]
# t = (1, 2, 3, 4, 5)
#
# print(l[1:3])
# print(t[1:2])
# print(l[:5:2])
# print(t[:5:2])

# str = ' abcd '
#
# print(list(str))
# print(str)

# 迭代用for循环实现遍历

# d = {'a': 1, 'b': 2, 'c': 3}
# for x in d:
#     print(x)
# for x in d.values():
#     print(x)
# for x, y in d.items():
#     print(x, y)

# 判断是否是可迭代对象

# from collections import Iterable
# print(isinstance('abc', Iterable))


# 列表生成式 [ x * x for x in range(1,11) if x %2 == 0]

# l = [x * x for x in range(1, 11) if x % 2 == 0]
# print(l)
#
# ll = [a + b for a in 'ABC' for b in 'XYZ']
# print(ll)
#
# d = {'a': '1', 'b': '2', 'c': '3'}
# dl = [dn + '=' + dm for dn, dm in d.items()] # 这里 + 连接的必须是str
# print(dl)
#
# sl = [aa if aa % 2 == 0 else -aa for aa in range(1, 11)]  #if 之后的结果 放在前面
# print(sl)

# 生成器 generator 定义方式 1.（生成式），2.函数yield关键字  ，调用方式 1.next 2.for in
#       调用generator 需要生成一个generator 对象 （就是创建一个对象指向 含yield 的函数）

# g = (x * x for x in range(1, 6) if x % 2 == 0)
# # print(next(g), next(g))
# # print(next(g))
# for a in g:
#     print(a)

# generator 定义方式之二 ：函数中有 yield 关键字

# def odd():
#     print("step1")
#     yield 1
#     print("step2")
#     yield 2
#     print("step3")
#     yield 3
#
# o = odd()
#
# print(next(o))
# print(next(o))
# print(next(o))

# 抛出异常

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a+b
#         n = n+1
#     return 'done'
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g',x)
#     except StopIteration as e:
#         print('The last value:',e.value)
#         break

# 迭代器：可直接作用于for，称迭代对象Iterable
# 用isinstance 判断是否是迭代对象

# from collections.abc import Iterable
# print(isinstance([],Iterable))
# from collections.abc import Iterator
# print(isinstance('abc',Iterator))
# print(isinstance(iter('abc'),Iterator))

# 将Iterable 转变为 Iterator,可被next()调用

# it = iter([1, 2, 3, 4])
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break

# 高阶函数
# def f(x):
#     if x < 0:
#         return -x
#     return x
# def add(x, y, f):
#     return f(x) + f(y)
#
# print(add(-1,3,f))

# map(函数，Iterable)函数,返回的是一个Iterator ,用list(Iterator)
# def f(x):
#     return x * x
#
# r = map(f, [1, 2, 3])
# print(r)
# print(list(r))

# reduce(函数，序列) 函数必须两个参数，作用在序列上，结果和序列下一个累积
# def f(x, y):
#     return x + y
#
# from functools import reduce
# reduce(f,[1,2,3,4,5])
# print(reduce(f,[1,2,3,4,5]))

# str = "abc"
# str[0].upper()
# str[1:].lower()
# print(str[0].upper()+str[1:].lower())

# def zh(name):
#     return name[0].upper()+name[1:].lower()
#
# r = list(map(zh,['ABC','aBc','acN']))
# print(r)

# filter（函数,序列）过滤函数，False就过滤，返回的是Itertor
# def not_null(s):
#     return s and s.strip()
# l = list(filter(not_null, ['a','b','','c','']))
# print(l)


# sorted(序列，key=函数)
# l = [1, 4, 5, 2, 3]
# print(sorted(l, key=abs))

# 返回函数

# def sum(*num):
#     def add():
#         temp = 0
#         for x in num:
#             temp = temp + x
#         return temp
#     return add  #返回的是add()的话就是一个结果了
#
# l1 = sum(1, 2, 3, 4, 5)
# l2 = sum(1, 2, 3, 4, 5)
# # print(l)
# # print(l())
# print(l1 == l2)

# 闭包的注意问题：内函数不引用循环变量或者以后会变化的变量，如果用，再用一个函数绑定

# def count():
#     l = []
#     for x in range(1,4):
#         def chen():
#             return x * x
#
#         l.append(chen)
#     return l
#
# l1, l2, l3 = count()
# print(l1(),l2(),l3())

# def count():
#     def f(i):
#         def g():
#             return i*i
#         return g
#     l = []
#     for x in range(1,4):
#         l.append(f(x))
#     return l
# l1, l2, l3 = count()
# print(l1(),l2(),l3())

# 匿名函数
#
# x = 3
# print(lambda x: x * x)
# f = lambda x: x * x
# print(f(3))

# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper

# 不需要传参数的装饰器
# def log(func):
#     def wep(*a, **b):
#         print("this is %s()" % func.__name__)
#         return func(*a, **b)
#     return wep
#
# @log
# def now():
#     print("前面有装饰器内容否")
#
# now()

# 需要传参数的装饰器
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#         return wrapper
#     return decorator

# def log(text):
#     def decorator(func):
#         def wep(*a, **b):
#             print("text:%s , This is %s()" %(text, func.__name__))
#             return func(*a, **b)
#         return wep
#     return decorator
#
# @log('ext')
# def now():
#     print("前面有装饰器内容否")
#
# now()

# 偏函数

# def int8(x,base=10):
#     return int(x,base = 8)
# print(int8('1000'))
#
# import functools
# int2 = functools.partial(int, base = 2)
# print(int2('1000'))

# 导入模块
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ' a test module '
#
# __author__ = 'Michael Liao'

import sys

# def test():
#     args = sys.argv
#     if len(args)==1:
#         print('Hello, world!')
#     elif len(args)==2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')
#
# if __name__=='__main__':
#     test()

# 类和实例

# class Student(object):
#
#     def __init__(self, name, score):
#         self.__name = name
#         self.score = score
#
#     def _print(self):
#         print(self.__name, self.score)
#
# stu = Student('zhang', 89)
# stu._print()
#
# stu.name = 'li'
# stu._print()

# 继承和多态
# class Animal(object):
#     def intro(self):
#         print("Animal is animal")
#
# class dog(Animal):
#     def intro(self):
#         print("dog is dong")
#
# d = dog().intro()

# 获取对象信息 1.type()  2.isinstance('','') 3.dir()

# print(type(124))
# print(type(abs))
# import types
# def f():
#     pass
# print(type(f) == types.FunctionType)


# ist = isinstance('a', str)
# print(ist)
# print(dir('abc'))

# 类的属性：动态语言在类中定义
# class Student(object):
#     name = 'Student'
# stu = Student().name
# print(stu)


# 使用_slots_
# class Stu(object):
#     __slots__ = ('name', 'age')
#
# s1 = Stu()
# s1.name = 'job'
# s1.age = 23
# s1.score = 35
# print(s1.name)
#
# def set_age(self, age):
#     self.age = age
#
# from types import MethodType
#
# s1.set_age = MethodType(set_age, s1)
# s1.set_age(25)
# print(s1.age)
#
# def set_score(self, score):
#     self.score = score
#
# Stu.set_score = set_score
#
# s1.set_score(10)
# print(s1.score)

# @property
# class Student(object):
#
#     @property
#     def age(self):
#         return self._age #属性名和方法名不能一样
#
#     @age.setter
#     def age(self, value):
#         if not isinstance(value,(int, float)):
#             raise ValueError("输入类型错误")
#         if value < 0 or value >100:
#             raise ValueError("输入范围有错")
#         self._age = value
#
# stu = Student()
# stu._age = 80
# print(stu._age)

# def get_score(self):
#     return score
#
# def set_score(self, value):
#     if not isinstance(value,(int, float)):
#         raise ValueError("输入类型错误")
#     if value < 0 or value >100:
#         raise ValueError("输入范围有错")
#     self.score = value

# stu = Student()
# stu.set_score(101)
# print(stu.score)

# 定制类

# class Student(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return 'Student name is %s' % self.name
#
# print(Student('zhang',23))

# class Student(object):
#     def __init__(self):
#         self.a = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a = self.a + 1
#         if self.a == 5:
#             raise StopIteration()
#
#         return self.a
# for x in Student():
#     print(x)

# class Fib(object):
#     def __getitem__(self, n):
#         if isinstance(n, int): # n是索引
#             a, b = 1, 1
#             for x in range(n):
#                 a, b = b, a + b
#             return a
#         if isinstance(n, slice): # n是切片
#             start = n.start
#             stop = n.stop
#             if start is None:
#                 start = 0
#             a, b = 1, 1
#             L = []
#             for x in range(stop):
#                 if x >= start:
#                     L.append(a)
#                 a, b = b, a + b
#             return L
#
# f = Fib()
# print(f[:4])

# class Student(object):
#     def __init__(self):
#         self.name = 'ace'
#     def __getattr__(self, item):
#         if item == 'score':
#             return 11
#
# stu = Student()
# print(stu.score)

# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __call__(self):
#         print("The name is %s" % self.name)
#
#
# stu = Student('zh')
# print(stu())  # 不传参数
#
# print(callable(Student))
# print(callable('adc'))

# 使用枚举类
from enum import Enum

# class Weekday(object):
#     sum = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
# day1 = Weekday.Mon
# print(day1)

# 使用元类 type()可实现在函数中创建类（函数名，继承的类，关联的方法）

Hello = type('Hello', (object,), dict(hello=fn))
