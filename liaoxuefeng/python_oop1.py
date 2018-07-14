'''
面向对象编程: 类和实例 / 访问限制 / 继承和多态/获取对象信息/实例属性和类属性
'''
import util.PrintUtil as pu
import util.LoggingUtil as logger
import types
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age =age
        self.score = score

    def team_score(self):
        print('{} 考了{}分'.format(self.name,self.score))
        return '{} 考了{}分'.format(self.name,self.score)

    def get_score_level(self):
        if self.score > 90:
            return "A"
        elif self.score > 80:
            return "B"
        else:
            return "继续努力"

tom = Student('tom',18,90)
lucy = Student('lucy',18,90)
tom.weight = '66.5kg'
pu.print_line_separator("类的实例->打印Student对象实例")
print(Student)
print(tom)
# print(lucy.weight)  # 我们只给tom实例赋了weight属性 所以打印lucy.weight 会 "AttributeError: 'Student' object has no attribute 'weight'"
print("name: {} ,age:{} ,score:{}分 ,体重:{}".format(tom.name,tom.age,tom.score,tom.weight))
print("{} ,属于:{}".format(tom.team_score(),tom.get_score_level()))

pu.print_line_separator("访问限制->属性的名称前加上两个下划线")
class Student2(object):
    def __init__(self,name,address,gender):
        self.name = name
        self.__address = address
        self.__gender = gender

    def get_address(self):
        return self.__address

    def set_address(self,address):
        self.__address = address

    def get_gender(self):
        return self.__gender

    def set_gender(self,gender):
        self.__gender = gender

    def __len__(self):
        return 111

jerry = Student2('jerry','塘苗路','male')
# print(jerry.__address)
jerry.set_address('塘苗路18号')
'''
表面上看，外部代码“成功”地设置了__age变量，但实际上这个__age变量和class内部的__age变量不是一个变量！内部的__age变量已经被Python解释器自动改成了_Student__age，而外部代码给bart新增了一个__age变量。不信试试：
>>> bart.get_name() # get_name()内部返回self.__name
'Bart Simpson'
'''
jerry.__age = 18
print(jerry.__dict__)
print("{} 家住: {}".format(jerry.name,jerry.get_address()))

bart = Student2('Bart','chain','male')
if bart.get_gender() != 'male':
    print('测试失败')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败')
    else:
        print('测试成功')


pu.print_line_separator("继承和多态")
'''
静态语言 vs 动态语言
对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，
都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。
'''

pu.print_line_separator("获取对象信息--type函数的使用")
def fn():
    pass
print("type(123) == int ? {}".format(type(123) == int))
print("type(fn)==types.FunctionType ? {}".format(type(fn)==types.FunctionType))
print("type(abs)==types.BuiltinFunctionType ? {}".format(type(abs)==types.BuiltinFunctionType))
print("type(lambda x: x)==types.LambdaType ? {}".format(type(lambda x: x)==types.LambdaType))
print("type((x for x in range(10)))==types.GeneratorType ? {}".format(type((x for x in range(10)))==types.GeneratorType))
print("isinstance(bart,Student2) ? {}".format(isinstance(bart,Student2)))
print("isinstance(bart,object) ? {}".format(isinstance(bart,object)))

pu.print_line_separator('获取一个对象的所有属性和方法..使用dir函数')
'''
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，
实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：len('ABC')  /  'ABC'.__len__()
'''
print(dir(bart))
print(len(bart))

pu.print_line_separator("hasattr / setattr /getattr")
print(hasattr(bart,'__gender'))
print(hasattr(bart,'name'))
print(setattr(bart,'name1','tt'))
print(getattr(bart,'name1'))
# print(getattr(bart,'name12'))  # 获取不存在的属性 会报错 "AttributeError: 'Student2' object has no attribute 'name12'"
print(getattr(bart,'name12','defaultname')) # 可以通过指定默认值 规避getattr获取不存在属性时的异常

# hasattr正确的使用模式..  只有在不知道对象信息的时候，我们才会去获取对象信息  知道的话就直接用
def readImage(fp):
    if hasattr(fp,'read'):
        # return readData(fp)
        pass
    return None
'''
假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，
但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
'''


pu.print_line_separator("实例属性和类属性")
class Student3(object):
    count = 0
    address = '地球村'
    def __init__(self,name):
        self.name = name
        Student3.count+=1




dada = Student3('dada')
print("实例的属性:{} 对象的属性:{}".format(dada.address,Student3.address))
dada.address = '火星'
print('给实例属性赋值后优先使用实例的属性: {}'.format(dada.address))
del dada.address
print('删除实例的属性后依然使用对象的属性: {}'.format(dada.address))

pu.print_line_separator("为了统计学生人数，可以给Student3类增加一个类属性，每创建一个实例，该属性自动增加：")

print("Student3.count : {}.".format(Student3.count))
if Student3.count != 1:
    print('测试失败!')
else:
    bart = Student3('Bart')
    if Student3.count != 2:
        print('测试失败!')
    else:
        lisa = Student3('Bart')
        if Student3.count != 3:
            print('测试失败!')
        else:
            print('Students:', Student3.count)
            print('测试通过!')