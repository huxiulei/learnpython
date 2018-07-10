import util.PrintUtil as pu
l1 = ["wangwu","lisi","zhangsan","zhaoliu"]
l2 = [89,90,77]
z = zip(l1,l2)

print("list(z): {}" .format(list(z)))
pu.print_line_separator()

print("type(z):{} ".format(type(z)))

for i in z:
    print(id(i))
    print(i,sep=" ")
pu.print_line_separator()

l3 = [i for i in list(z)]
print("type(l3):{} len(l3):{}".format(type(l3),len(l3)))
print(l3)

print(help(zip))