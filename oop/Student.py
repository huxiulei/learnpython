import util.PrintUtil as pu


class Student():
    name = "huhuhu"
    age = 18
    address = "西湖区塘苗路"
    # 其实python的私有不是真正意义上的私有 只是使用了 name mangling技术
    __nickname = "xixi"


    def __init__(self):
        self.name = "laohu"
        self.age=27

    def sayHello(self):
        self.name = "hu"
        self.address = "华星现代产业园"
        print("hello {} , age : {} ,address:{}".format(self.name,self.age,self.address))
        print("访问类的成员属性(非实例的)使用__class__.address : {}".format(__class__.address))


class Student2(Student):
    name = None
    age = 1
    # pass


s = Student()
print("s.name = %s,s.age = %s"%(s.name,s.age))
#print("s.nickname = ".format(s.__nickname))
s.sayHello()

pu.print_line_separator("访问私有属性")

# 其实python的私有不是真正意义上的私有 只是使用了 name mangling技术 如果真要访问的话 可以使用下面方法
print(Student.__dict__)
print("访问私有属性 nickname: {0}".format(s._Student__nickname))
pu.print_line_separator()

# 可以直接把Student2当作参数传递, Python是弱语言 若sayHello中有用到Student2中不存在的属性 会报错
Student.sayHello(Student2)
