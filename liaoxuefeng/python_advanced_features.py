'''
Python高级特征   切片/迭代/列表生成式/生成器/迭代器
'''
import os
import util.PrintUtil as pu
def trim(str):
    str_len = len(str)

    print("str_len:{}".format(str_len))
    if str == ' ':
        return ''
    if str_len == 0:
        return ''
    index = 0
    temp_str = ''
    while index <= (str_len - 1):
        if str[index] == ' ' and temp_str == '':
            pass
        else:
            print("str[index:1] : {}".format(str[index:index+1]))
            temp_str = temp_str + str[index:index+1]
        index += 1
    str_len2 = len(temp_str)
    temp_str2 = ''
    while str_len2 > 0:
        if(temp_str[str_len2-1:str_len2] == ' ' and temp_str2 == ''):
            pass
        else:
            print("temp_str[str_len2-1:str_len2] : {}".format(temp_str[str_len2-1:str_len2]))
            temp_str2 = temp_str2 + temp_str[str_len2-1:str_len2]
        str_len2 -= 1


    return temp_str2


after_trim_str = trim("  ab c  ")
print("去除左右空格后的字符串是{}".format(after_trim_str))

pu.print_line_separator()

# 去除一个字符串的前后空格，中间的忽略
def trim2(s):
    if s[:1] == " ":
        return trim2(s[1:])
    elif s[-1:] == " ":
        return trim2(s[:-2])
    else:
        return s
print(trim2(" he l lo  "))
pu.print_line_separator()

def trim3(s):
    i = 0
    j = len(s)
    while s[i:i+1] == ' ':
        i+=1
    while s[j-1:j] == ' ':
        j-=1
    s = s[i:j]
    return s

trim3_str = trim3("  A BC  ")
print("trim3_str:{}".format(trim3_str))

pu.print_line_separator("找到list中的最小值和最大值返回tuple类型")
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMaxFromList(L):
    if len(L) == 0:
        return (None,None)
    if(len(L) == 1):
        return (L[0],L[0])

    min = L[0]
    max = L[0]
    for x in L:
        if x < min:
            min = x
        if x > max:
            max = x
    return (min,max)


print("list中最小和最大分别是： {}" .format(findMinAndMaxFromList([33,1,22,5])))

dirlist = [d for d in os.listdir(".")]
print(dirlist)

dx = {"x":'X',"y":'Y'}
print([k + "=" + v for k,v in dx.items()])


LL = ['Hello', 'World', 18, 'Apple', None]
LL_after = [ll.lower() for ll in LL if isinstance(ll,(str))]
print(LL_after)

pu.print_line_separator("斐波拉契数列")
# 斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(5)


pu.print_line_separator("杨辉三角")

# 杨辉三角
def triangles():
    L = [1]
    while True:
        yield L
        L= [(L + [0])[i] + ([0] + L)[i] for i in range(len(L)+1)]


for i in range(10):
    print(next(triangles()))
