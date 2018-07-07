class A():
    pass


class B(A):
    pass

# 打印出A类的所有方法包括父类方  MRO (MethodResolutionOrder)
print(A.mro())

print(B.mro())

'''
Python允许多继承   但是会造成混乱   菱形继承/钻石继承问题  参考:https://www.cnblogs.com/whatisfantasy/p/6046991.html

多态和多态性  参考:https://www.cnblogs.com/luchuangao/p/6739557.html

Mixin概念  参考: https://www.zhihu.com/question/20778853
'''

print(help(setattr))