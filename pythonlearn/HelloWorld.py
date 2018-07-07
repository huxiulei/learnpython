def hello_world():
    print("Hello Python")

hello_world()


a = ["1","2","3"]
b = ["a","b","c"]
m = (m+n for m in a for n in b)
n = [m+n for m in a for n in b]
print("a: {}".format(a))
print("id(a): {}".format(id(a)))
print("b: {}".format(b))
print("m: {}".format(m))
print("id(m) : {}, type(m):{}".format(id(m),type(m)))
print("id(n) : {}, type(n):{}".format(id(n),type(n)))

#一只敏捷的棕色狐狸跳到了一只懒狗身上。该句据说是包含所有26个字母的最短的句子。
print('The quick brown fox', 'jumps over', 'the lazy dog')

print('100 + 200 =', 100 + 200)

#name = input("请输入你的名称: ")
#print("欢迎: ",name)

print('''
hha
hhe
heih
xix
''')


'''
加r和不加''r是有区别的:
'r'是防止字符转义的 如果路径中出现'\t' , '\n'的话 不加r的话\t,\n 就会被转义 而加了'r'之后就能保留原有的样子
在字符串赋值的时候 前面加'r'可以防止字符串在赋值的时候不被转义 原理是在转义字符前加'\'
'''
s4 = r'''Hello,\n
Lisa!'''
print(s4)

# 对百分号转义的话 也要使用%  一个参数的话可以省了括号
print('增长率%s%% 你很棒%s'%(7,'tom'))