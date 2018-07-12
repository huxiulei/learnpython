import shelve
import util.PrintUtil as pu
f = open(r'HelloWorld.py','r',encoding='utf-8')
# 读取全部
# print(f.read())
f.close()

'''
python读取文件时提示"UnicodeDecodeError: 'gbk' codec can't decode byte 0x80 in position 205: illegal multibyte sequence"
解决办法1:  FILE_OBJECT= open('order.log','r', encoding='UTF-8')
解决办法2:  FILE_OBJECT= open('order.log','rb')
'''
with open(r'HelloWorld.py','r',encoding='utf-8') as f:
    lines = list(f)
    # 把整个文件内容当作一个list,然后遍历读
    for line in lines:
        # print(line)
        pass

pu.print_line_separator()

# r代表后面的字符串不做转义   writelines是不换行的
with open(r'test.txt','a') as f:
    # writelines参数可以是list
    l = ["I","Love","Python"]
    f.writelines('hahaha')
    f.writelines('heihei')
    f.writelines(l)

with open(r'test.txt','r') as test:
    print(test.read())

# print(help(shelve))


# shv = shelve.open(r'tt.db')
# shv['one'] = 1
# shv['two'] = 2
# shv.close()


with shelve.open(r'tt.db') as shv:
    # print(shv['one'])
    # print(shv['two'])
    print(shv['one'])
    shv['one'] = 100
    print(shv['one'])

with shelve.open(r'tt.db') as shv:
    # print(shv['one'])
    # print(shv['two'])
    print(shv['one'])
    shv['one'] = 1
    print(shv['one'])
