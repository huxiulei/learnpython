#!/usr/bin/env python
# coding=utf-8
import util.PrintUtil as pu
'''
位置参数：

调用函数时所传参数的位置必须与定义函数时参数的位置相同

关键字参数：

使用关键字参数会指定参数值赋给哪个形参，调用时所传参数的位置可以任意

*位置参数：可接受任意数量的位置参数(元组)；只能作为最后一个位置参数出现，其后参数均为关键字参数

**关键字参数：可接受任意数量的关键字参数(字典)；只能作为最后一个参数出现

默认参数：默认参数的赋值只会在函数定义的时候绑定一次，默认值不会再被修改

'''


def print_hello(name, sex):
    sex_dict = {1: u'先生', 2: u'女士'}
    print('hello %s %s, welcome to python world!' %(name, sex_dict.get(sex, u'先生')))

'''
一、位置参数
调用函数时根据函数定义的参数位置来传递参数。
'''
# 两个参数的顺序必须一一对应，且少一个参数都不可以
# print_hello('tanggu', 1)


'''
二、关键字参数
用于函数调用，通过“键-值”形式加以指定。可以让函数更加清晰、容易使用，同时也清除了参数的顺序需求。
'''
# 以下是用关键字参数正确调用函数的实例
# print_hello('tanggu', sex=2)
# print_hello(name='tanggu', sex=1)
# print_hello(sex=1, name='tanggu')

# 以下是错误的调用方式
# print_hello(sex=1, name='tanggu')
# print_hello(name='tanggu',1)
# print_hello(sex=1, 'tanggu')


'''
三、默认参数
用于定义函数，为参数提供默认值，调用函数时可传可不传该默认参数的值（注意：所有位置参数必须出现在默认参数前，包括函数定义和调用）
'''
# 正确的默认参数定义方式--> 位置参数在前，默认参数在后
def print_hello2(name, sex=1):
    pass

# 错误的定义方式
# def print_hello2(sex=1, name):
#     pass

# 调用时不传sex的值，则使用默认值1
# print_hello2('tanggu')

# 调用时传入sex的值，并指定为2
# print_hello2('tanggu', 2)


'''
四、可变参数
定义函数时，有时候我们不确定调用的时候会传递多少个参数(不传参也可以)。此时，可用包裹(packing)位置参数，或者包裹关键字参数，来进行参数传递，会显得非常方便。
'''
# 1、包裹位置传递  我们传进的所有参数都会被args变量收集，它会根据传进参数的位置合并为一个元组(tuple)，args是元组类型，这就是包裹位置传递。
def func(*args):
    print(type(args))
a=1
b=2
c=3
# func()
# func(a)
func(a, b, c)


pu.print_line_separator()

# 2、包裹关键字传递 kargs是一个字典(dict)，收集所有关键字参数
def func(**kargs):
    print(type(kargs))

# func(a=1)
func(a=1, b=2, c=3)


'''
五、解包裹参数
*和**，也可以在函数调用的时候使用，称之为解包裹(unpacking)
'''

# 1、在传递元组时，让元组的每一个元素对应一个位置参数
def print_hello(name, sex):
    print ("name = {} ,sex = {}".format(name, sex))

args = ('tanggu', '男')
print("type(args):  {}".format(type(args)))
#print_hello(*args)


# 2、在传递词典字典时，让词典的每个键值对作为一个关键字参数传递给函数
def print_hello3(**kargs):
    print(kargs)

kargs = {'name': 'tanggu', 'sex': u'男'}
# {'name': 'tanggu', 'sex', u'男'}
print_hello3(**kargs)


'''
六、位置参数、默认参数、可变参数的混合使用
基本原则是：先位置参数，默认参数，包裹位置，包裹关键字(定义和调用都应遵循)
'''
def func(name, age, sex=1, *args, **kargs):
    print (name, age, sex, args, kargs)


# tanggu 25 1 ('music', 'sport') {'class'=2}
func('tanggu', 25, 2, 'music', 'sport', key1='value1')



pu.print_line_separator()

# Python中 *args 和 **kwargs 的区别
def foo(*args, **kwargs):
    print ('args = ', args)
    print ('kwargs = {}'.format(kwargs))
    print ('---------------------------------------')

if __name__ == '__main__':
    foo(1,2,3,4)
    foo(a=1,b=2,c=3)
    foo(1,2,3,4, a=1,b=2,c=3)
    foo('a', 1, None, a=1, b='2', c=3)
'''
输出结果如下:
args =  (1, 2, 3, 4) 
kwargs =  {} 
--------------------------------------- 
args =  () 
kwargs =  {'a': 1, 'c': 3, 'b': 2} 
--------------------------------------- 
args =  (1, 2, 3, 4) 
kwargs =  {'a': 1, 'c': 3, 'b': 2} 
--------------------------------------- 
args =  ('a', 1, None) 
kwargs =  {'a': 1, 'c': 3, 'b': '2'}


可以看到，这两个是Python中的可变参数。*args 表示任何多个无名参数，它是一个tuple；**kwargs 表示关键字参数，它是一个dict。
并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前，像foo(a=1, b='2', c=3, a', 1, None, )这样调用的话，会提示语法错误“SyntaxError: non-keyword arg after keyword arg”。
'''


pu.print_line_separator()

def kw_dict(**kwargs):
    return kwargs

# 其实python中就带有dict类，使用dict(a=1,b=2,c=3)即可创建一个字典了。
print (kw_dict(a=1, b=2, c=3) == {'a': 1, 'b': 2, 'c': 3})


pu.print_line_separator()




def foo(x,*args,a=4,**kwargs):  #使用默认参数时，注意默认参数的位置要在args之后kwargs之前
    print(x)
    print(a)
    print(args)
    print(kwargs)

foo(1,5,6,7,8,y=2,z=3)  #调用函数，不修改默认参数
'''
打印结果如下:
1   #x的值
4   #a的值
(5, 6, 7, 8)   #*args的值
{'y': 2, 'z': 3}    ##kwargs的值


##注意：当需要修改默认参数时，要调整默认参数的位置，要放在args之前即可，但不可放在开头。
如: def foo(x,a=4,*args,**kwargs):
    
'''