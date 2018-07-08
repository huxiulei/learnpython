class Person():
    '''
    这里是关于类Person的文档说明
    __init__  __call__    __str__  属于魔法/魔术函数   会在适当时机自动触发
    '''

    def __init__(self,name):
        self._name = name
        print("Person 实例化")

    def __call__(self, *args, **kwargs):
        print(self.name)

    def __str__(self):
        return self.name

    def __setattr__(self, name, value):
        print("设置属性:{}".format(name))
        # 本来__setattr__ 该函数就是设置属性的时候会调用的 所以下面的方式 会死循环
        # self.name = value
        # 为了避免死循环可以通过下面方式调用
        super().__setattr__(name,value)

    # 进行大小判断时触发的魔术函数
    def __gt__(self, other):
        print("哈哈 {0}比{1}大吗？".format(self,other))
        return self.name > other._name

    # 类方法  不用实例化 Person.play() 调用 同时也支持实例调用
    @classmethod
    def play(cls):
        print(cls)
        print("playing....")

    # 静态方法  不用实例化
    @staticmethod
    def say():
        print("saying....")


    def fget(self):
        return self._name * 2
    def fset(self,name):
        self._name = name

    def fdel(self):
        self._name = "noname"

    name = property(fget,fset,fdel,"对name的操作")


# 注意缩紧 不然会报错， python就是通过缩紧来判断代码层级
p1 = Person("p1")
p1.name = "huhuhu"
print(p1.name)

print(Person.__doc__)
# 需要定义__call__方法才能把类当作函数使用
p1()

# <__main__.Person object at 0x10268bba8>
# 定义 __str__方法 可以按照自定义打印
print(p1)


print("**" * 20)

person1 = Person("one")
person2 = Person("two")
print(person1 > person2)


print("**" * 20)

Person.say()
person1.say()
Person.play()
person1.play()