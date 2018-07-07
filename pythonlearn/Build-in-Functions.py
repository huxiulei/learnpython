import struct
'''
Python内置参数
'''

def print_line_separator():
    print(" ")
    print("**" * 30)
    print(" ")



print(dir())

print("")
print("*" * 50)
print(dir(struct))


help(str())


print("*" * 50)
print(str.__doc__)

print_line_separator()

help(print)