import util.PrintUtil as pu

# 字符编码的说明以下链接
# https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000
ord_A = ord('A')
print(ord_A)

chr_88 = chr(88)
print(chr_88)

pu.print_line_separator()

# 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))

pu.print_line_separator()

print(len('中文')) #计算字符长度
print(len('中午'.encode('utf-8')))

pu.print_line_separator()

s1 = 78
s2 = 85
r = s1 / s2
print('百分比%.2f%%' %r) # 保留两位小数的话 使用 %.2f

r = (s2-s1)/s1*100
print('你好,%s的成绩提高了%.2f%%' % ('小明',r))


'''
    以下list的使用说明 有序的列表 下标访问元素时,如果越界会报"IndexError: list index out of range"错
    tuple 也是有序的列表 没有append()，insert()这样的方法 因为不能修改
    tuple和list非常类似，但是tuple一旦初始化就不能修改
'''
pu.print_line_separator("以下list/tuple的使用")

classmates = ['tom','jerry','lucy']
print("访问list的最后一个元素,下标可以使用classmates[len(classmates) - 1] : {}".format(classmates[len(classmates) - 1]))
print("也可以使用下表为 -1来获取list的最后一个元素: {}".format(classmates[-1]))
# 在下标为1的位置插入一个元素
classmates.insert(1,"jack")
print(classmates)
# 删除list末尾的元素并返回
classmates.pop()
classmates.sort()

pu.print_line_separator()

cms = ('Michael', 'Bob', 'Tracy')
'''
定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
'''
aa = (1)
print(type(aa))
aa = (1,)
print(aa)
print(type(aa))

'''
表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，
所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。
'''
tupleA = ("a","b",["1","2"])
print(tupleA)
tupleA[2][0] = "X"
tupleA[2][1] = "Y"
print(tupleA)
ss=([1,2,3])
print("type(ss) : {}".format(type(ss)))
ss[0] = [5,6,7]
print("ss : {}".format(ss))



L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][1])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][-1])
print(L[2][len(L[2]) - 1])

pu.print_line_separator("以下条件判断")

# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x=(1,)
if x:
    print('True')

print("使用int()函数转化str为int: {}".format(int("33")))



pu.print_line_separator("以下循环")
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print("100以内所有奇数之和: {}".format(sum))

# continue的作用是提前结束本轮循环，并直接开始下一轮循环。
# break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)


pu.print_line_separator("以下dict/set使用说明")
'''
和list比较，dict有以下几个特点：
    查找和插入的速度极快，不会随着key的增加而变慢；
    需要占用大量的内存，内存浪费多。
而list相反：
    查找和插入的时间随着元素的增加而增加；
    占用空间小，浪费内存很少。
    所以，dict是用空间来换取时间的一种方法。
dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：

所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

'''
dictA = {'tom':90,'lucy':80}
print(dictA)
#print(dictA["tom1"])  # 没有key的话 会报错 KeyError
print(dictA.get('jerry',70)) # 没有的话返回默认值70  不指定默认值的话 返回None

setA = set([1,2,2,3])
print(setA)
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。
set1 = set([1,2,3])
set2 = set([2,3,4])
print("set1,set2交集: {}".format(set1 & set2))
print("set1,set2并集: {}".format(set1 | set2))
# TypeError: unhashable type: 'list'
# set1.add([5,6])