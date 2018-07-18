'''
python文件操作: 文件读写 /StringIO/BytesIO / 操作文件和目录 / 序列化
'''
import util.PrintUtil as pu
from io import StringIO
from io import BytesIO
import os
import json

'''
很多时候，数据读写不一定是文件，也可以在内存中读写。

StringIO顾名思义就是在内存中读写str。

要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
'''
pu.print_line_separator("StringIO使用")
f = StringIO()
f.writelines('''
hello
python
io
''')
s = f.getvalue()
print(s)


pu.print_line_separator("使用StringIO读取")
f = StringIO('我是StringIO字符串\nbyebye')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


pu.print_line_separator("BytesIO的使用")
b = BytesIO()
b.write('中午'.encode('utf-8'))
print(b.getvalue())


pu.print_line_separator("操作文件和目录")
print("如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。 当前是:{}".format(os.name))
# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
# print(os.uname())
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
print(os.environ)
print('使用os.environ.get(\'key\')获取指定环境变量:{}'.format(os.environ.get('APPDATA')))
'''
操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

# 查看当前目录的绝对路径:
>>> os.path.abspath('.')
'/Users/michael'
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'
# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')

把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
拆分文件名
>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')
os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：

>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')


'''

pu.print_line_separator('列出当前目录下的所有文件夹')
# print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.')])


'''
练习
利用os模块编写一个能实现dir -l输出的程序。
编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
'''

def getFiles(path = '.'):
    print('当前目录:{}'.format(path))
    for x in os.listdir(path):
        absPath = os.path.join(path,x)
        # print('absPath:{}'.format(absPath))
        if os.path.isdir(x):
            getFiles(absPath)
        else:
            print(absPath)

print(getFiles('D:\PycharmProjects\learnpython'))
pu.print_line_separator()
# print(os.path.isdir('D:\PycharmProjects\learnpython\liaoxuefeng'))
# print(os.listdir('D:\PycharmProjects\learnpython\liaoxuefeng'))



'''
python中有 pickle序列化(pickle.dumps(d) / pickle.loads(s))  但是可能在不同的版本中兼容性不同 故此处不举例了

'''
pu.print_line_separator('json序列化对象')

class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

def student2dict(stu):
    return {'name':stu.name,'age':stu.age}

def dict2student(d):
    return Student(d['name'],d['age'])

stu = Student('tom',15)
print(json.dumps(stu,default=student2dict))

pu.print_line_separator('json反序列化')
stu_str = '{"name": "tom", "age": 15}'
print(json.loads(stu_str,object_hook=dict2student))


obj = dict(name='小明', age=20)
s_obj = json.dumps(obj, ensure_ascii=True)
s_obj2 = json.dumps(obj, ensure_ascii=False)
# 对含有中文的dict进行json序列化:{"name": "\u5c0f\u660e", "age": 20}
print('对含有中文的dict进行json序列化:{}'.format(s_obj))
# 对含有中文的dict进行json序列化:{"name": "小明", "age": 20}
print('对含有中文的dict进行json序列化:{}'.format(s_obj2))