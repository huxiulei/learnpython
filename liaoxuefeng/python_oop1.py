'''
面向对象编程: 类和实例 / 访问限制 / 继承和多态/获取对象信息/实例属性和类属性
'''
import util.PrintUtil as pu
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
pu.print_line_separator("打印Student对象实例")
print(Student)
print(tom)
# print(lucy.weight)  # 我们只给tom实例赋了weight属性 所以打印lucy.weight 会 "AttributeError: 'Student' object has no attribute 'weight'"
print("name: {} ,age:{} ,score:{}分 ,体重:{}".format(tom.name,tom.age,tom.score,tom.weight))
print("{} ,属于:{}".format(tom.team_score(),tom.get_score_level()))
pu.print_line_separator()