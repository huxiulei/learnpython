'''
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/00143191235886950998592cd3e426e91687cdae696e64b000
使用__slots__
使用@property
多重继承
定制类
使用枚举类
使用元类
'''
import util.PrintUtil as pu
from enum import Enum

'''
把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
'''
class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    def __init__(self,name):
        self.name = name

    '''
    默认如果直接打印实例的话 会输出 <__main__.Student object at 0x107d16668>    __str__函数 自定义输出格式
    但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看
    这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。

    解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：

    class Student(object):
        def __init__(self, name):
            self.name = name
        def __str__(self):
            return 'Student object (name=%s)' % self.name
        __repr__ = __str__
    '''
    def __str__(self):
        return 'Student name is :{} '.format(self.name)

    def __repr__(self):
        return 'Student name is :{} '.format(self.name)

    def __call__(self, *args, **kwargs):
        print('my name is %' %self.name)


pu.print_line_separator('通过@property来访问属性，并可以设置属性校验')
s = Student("Tom")
s.score = 99
print(s.score)
# s.score = 110  # 超过限制的话 就会rasie异常
print(s)

pu.print_line_separator('通过callable函数判断一个对象是否可调用')
print(callable(Student('Jerry'))) # 此时返回的是 False  但Student类中定义 __call__方法后 打印即是Ture
print(callable(max))


pu.print_line_separator('利用完全动态的__getattr__，我们可以写出一个链式调用')

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print("Chain().status.user.timeline.list : {}".format(Chain().status.user.timeline.list))





# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name,member in Month.__member__.item():
#     print('name = % member = % value = %' %(name,member,member.value))
