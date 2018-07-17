'''
python 错误  测试  和调试
'''
import unittest
import util.PrintUtil as pu
from functools import reduce

def str2num(s):
    # 此处改为 float() 或者是 eval (兼容int()和float())
    return eval(s.strip())

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

pu.print_line_separator("以下用于单元测试")


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score < 0:
            raise ValueError('分值不能小于0')
        if self.score > 100:
            raise ValueError('分值不能高于100')

        if self.score >= 60 and self.score < 80:
            return 'B'
        elif self.score >= 80 and self.score < 100:
            return 'A'
        else:
            return 'C'


# class TestStudent(unittest.TestCase):
#
#     def test_80_to_100(self):
#         s1 = Student('Bart', 80)
#         s2 = Student('Lisa', 100)
#         self.assertEqual(s1.get_grade(), 'A')
#         self.assertEqual(s2.get_grade(), 'A')
#
#     def test_60_to_80(self):
#         s1 = Student('Bart', 60)
#         s2 = Student('Lisa', 79)
#         self.assertEqual(s1.get_grade(), 'B')
#         self.assertEqual(s2.get_grade(), 'B')
#
#     def test_0_to_60(self):
#         s1 = Student('Bart', 0)
#         s2 = Student('Lisa', 59)
#         self.assertEqual(s1.get_grade(), 'C')
#         self.assertEqual(s2.get_grade(), 'C')
#
#     def test_invalid(self):
#         s1 = Student('Bart', -1)
#         s2 = Student('Lisa', 101)
#         with self.assertRaises(ValueError):
#             s1.get_grade()
#         with self.assertRaises(ValueError):
#             s2.get_grade()

# if __name__ == '__main__':
#     unittest.main()


pu.print_line_separator("以下是文档注释测试")

# mydict2.py
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    # def __getattr__(self, key):
    #     try:
    #         return self[key]
    #     except KeyError:
    #         raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()