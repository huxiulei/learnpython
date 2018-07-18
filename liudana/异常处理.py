import re
value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

try:
    num = input("请输入被除数: ")
    result = value.match(num)
    if is_number(num):
        print("用户输入值:{}".format(num))
    else:
        raise ValueError("非法的值输入")

    # print(100 / int(num))

except ValueError as ve:
    print("输入的值有误: {}".format(ve))
    exit()
except Exception as e:
    print("异常了 : {}".format(e))
    exit()
finally:
    print("异常测试finally输出")


