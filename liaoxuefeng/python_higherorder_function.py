'''
函数式编程:

既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

一个最简单的高阶函数：

def add(x, y, f):
    return f(x) + f(y)

    filter()函数返回的是一个Iterator，也就是一个惰性序列,所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
    filter()的作用是从一个序列中筛出符合条件的元素。由于filter()使用了惰性计算，所以只有在取filter()结果的时候，才会真正筛选并每次返回下一个筛出的元素。

sorted()也是一个高阶函数。用sorted()排序的关键在于实现一个映射函数。


'''

from functools import reduce
import util.PrintUtil as pu
import time, functools

def add(x, y, f):
    return f(x) + f(y)

pu.print_line_separator("高阶函数add调用")

result = add(-1,4,abs)
print("高阶函数add调用结果: {}".format(result))



pu.print_line_separator("高阶函数求两个list中最大\最小值的和")
def listPlus(list1,list2,plus1,plus2):
    return plus1(list1) + plus2(list2)

list1 = [1,4,5]
list2 = [100,200,500]
listMaxPlus = listPlus(list1,list2,max,min)
print("求两个list最大元素之和: {}".format(listMaxPlus))

pu.print_line_separator()
max, min = min, max
print(max(1, 2, 3, 4, 5))
print(min(1, 2, 3, 4, 5))


pu.print_line_separator("Python内置函数 map()/reduce()使用")
def f(x):
    return x * x

list1 = map(f,[1,2,3,4,5])
print(list(list1))


str1 = map(str,[1,2,3,4,5])
print(list(str1))



DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

print(str2int("123123"))

#还可以用lambda函数进一步简化成：

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(list(map(char2num, "123456")))

pu.print_line_separator()

# 首字母大写 其他小写
def normalize(name):
    temp_str = name[:1].upper() + name[1:len(name)].lower()
    return temp_str


print(list(map(normalize,['adam', 'LISA', 'barT'])))


pu.print_line_separator("Python内建的filter()函数用于过滤序列")
def is_odd(x):
    return x % 2 == 1

print(list(filter(is_odd,[1,2,3,4,5,6,7,8,9])))

def not_empty(s):
    return s and s.strip()  # 此处是过滤非空后在去空格  否则:AttributeError: 'NoneType' object has no attribute 'strip'
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))


pu.print_line_separator("通过高阶函数实现求素数")
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x:x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)

for n in primes():
    if n < 100:
        print(n)
    else:
        break


pu.print_line_separator("回数是指从左向右读和从右向左读都是一样的数，例如12321，909")
def is_palindrome(s):
    s = str(s)
    return s == s[::-1]

print(list(filter(is_palindrome,range(1,100))))

pu.print_line_separator("高阶函数sorted的使用")
print(sorted(['Acd','Tom','lucy','jerrY','JACK','ROY'],key=str.lower))
print(sorted(['Acd','Tom','lucy','jerrY','JACK','ROY'],key=str.lower,reverse=True)) # 排序后的结果倒过来



pu.print_line_separator("对元组中的数据按照名称\分数进行排序")
L1 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def sorted_by_name(t):
    return t[0];
def sorted_by_score(t):
    return t[1];
print(sorted(L1,key=sorted_by_name,reverse=True))
print(sorted(L1,key=sorted_by_score))
print(sorted(L1,key=tuple))


pu.print_line_separator("利用闭包返回一个计数器函数，每次调用它返回递增整数")
def createCounter():
    def cc():
        i = 1
        while True:
            yield i
            i = i + 1
    it = cc()
    def counter():
        return next(it)
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


def count():
    fs = []
    for i in range(1, 3):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2 = count()
print(f1())
print(f2())

pu.print_line_separator("匿名函数")
print(list(filter(lambda n : n % 2 == 1, range(1, 20))))
print(list(filter(lambda n : n % 2, range(1, 20))))
print(list(filter(lambda n : n % 3, range(1, 20))))
print(list(filter(lambda n : n % 3 == 0, range(1, 20))))


pu.print_line_separator("装饰器")
print("函数对象有一个__name__属性，可以拿到函数createCounter的名字：{}".format(createCounter.__name__))

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        start = time.time()
        r = fn(*args,**kw)
        consumed = (time.time() - start) * 1000
        print('%s executed in %s ms'%(fn.__name__,consumed))
        return r
    return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
print("f = {},s = {}".format(f,s))
if f != 33:
    print('{} 测试失败!'.format(f.__name__))
elif s != 7986:
    print('{} 测试失败!'.format(s.__name__))
else:
    print('{} 测试通过!'.format(fast.__name__))


pu.print_line_separator("装饰器实现日志输出")

def log(*remark):
    def decorator(fn,*args,**kw):
        @functools.wraps(fn)
        def wrapper(*args,**kw):
            if remark and len(remark) > 0:
                print('{}正在执行函数:{}'.format(remark[0], fn.__name__))
            else:
                print('匿名正在执行函数:{}'.format(fn.__name__))
            return fn(*args,**kw)
        return wrapper
    return decorator

@log()
def slow2(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

print(slow2(1,2,3))

pu.print_line_separator("使用funtools.partial实现偏函数")
# 所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
int2 = functools.partial(int,base = 2)
print(int2('1000000'))