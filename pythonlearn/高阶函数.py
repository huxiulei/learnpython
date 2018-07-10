import util.PrintUtil as pu
l1 = ["wangwu","lisi","zhangsan","zhaoliu"]
l2 = [89,90,77]
z = zip(l1,l2)
print("list(z): {}" .format(list(z)))
pu.print_line_separator()

'''
    和Python2的区别（一）：返回的是一个迭代器，而不是一个list本身
    上面已经打印了一次了 所以下面再遍历的话就是[]  因为迭代器只能遍历一次
'''
print("type(z):{} ".format(type(z)))

for i in z:
    print(id(i))
    print(i,sep=" ")
pu.print_line_separator()

l3 = [i for i in list(z)]
print("type(l3):{} len(l3):{}".format(type(l3),len(l3)))
print(l3)

# print(help(zip))