import math
import util.PrintUtil as pu
'''
定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。
'''

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
alias_abs = abs
print(alias_abs(-1))

print(hex(12)) # 0xc 十六进制0x开头

pu.print_line_separator("定义函数")

def my_abs(x):
    # 不加这个判断的话 TypeError: '>' not supported between instances of 'str' and 'int' 会是这个错误
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type ')
    if x > 0:
        return x
    else:
        return -x


print(my_abs(1))
print(my_abs(-11))
# print(my_abs('x'))

pu.print_line_separator()



def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx,ny

'''
但其实这只是一种假象，Python函数返回的仍然是单一值： 如 print(xy)
原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
'''
x, y = move(100, 100, 60, math.pi / 6)
xy = move(100, 100, 60, math.pi / 6)
print(x, y)
print(xy)

pu.print_line_separator()


## 计算指定数xx的n次方
def power(xx, n=2):
    if not (isinstance(xx,(int,float)) and isinstance(n,(int,float))):
        raise TypeError('只能传递数字类型参数')
    s = 1   # 5
    while n > 0:
        n = n - 1 # 0
        s = s * xx # 5 * 5
        print("n = {} ,s = {}".format(n,s))
    return s


print(power(5,2))
print(power(3))
pu.print_line_separator("函数的参数")

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1, 2, 3]
print(calc(*nums,4,5))

'''
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


pu.print_line_separator("递归函数")


def fact(f):
    if f == 1:
        return 1
    else:
        return f * fact(f-1)

print(fact(4)) #RecursionError: maximum recursion depth exceeded in comparison
'''
解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。

上面的fact(n)函数由于return n * fact(n - 1)引入了乘法表达式，所以就不是尾递归了。要改成尾递归方式，需要多一点代码，主要是要把每一步的乘积传入到递归函数中：

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用。

fact(5)对应的fact_iter(5, 1)的调用如下：

===> fact_iter(5, 1)
===> fact_iter(4, 5)
===> fact_iter(3, 20)
===> fact_iter(2, 60)
===> fact_iter(1, 120)
===> 120

尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。

遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
'''
def fact1(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact1(10))


pu.print_line_separator("递归实现汉诺塔")
def hnt(n,a,b,c):
    if n == 1:  # 如果a只有1盘子
        print(a, '-->', c);  # 直接把盘子从a移到c
    else:  # 如果a有n个盘子(n > 1)，那么分三步
        hnt(n - 1, a, c, b)  # 先把上面n-1个盘子，借助c，从a移到b
        hnt(1, a, b, c)  # 再把最下面的1个盘子，借助b，从a移到c
        hnt(n - 1, b, a, c)  # 最后把n-1个盘子，借助a，从b移到c

hnt(4,'A','B','C') # 测试