import functools


# 构建不带参数的装饰器
def logging(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        print("%s called" % func.__name__)
        result = func(*args, **kwargs)
        print("%s end" % func.__name__)
        return result
    return decorator

# 使用装饰器
@logging
def test01(a, b):
    print("in function test01, a=%s, b=%s" % (a, b))
    return 1

# 使用装饰器
@logging
def test02(a, b, c=1):
    print("in function test02, a=%s, b=%s, c=%s" % (a, b, c))
    return 1

# test01(1, 2)
# test02(1, 2)


# 装饰器实例: 函数缓存
def funccache(func):
    cache = {}

    @functools.wraps(func)
    def _inner(*args):
        print(args)
        if args not in cache:
            cache[args] = func(*args)
        else:
            print("in cache")
        return cache[args]
    return _inner

# 使用装饰器
@funccache
def test08(a, b, c):
    # 其他复杂或耗时计算
    return a + b + c


test08(1, 2, 3)
test08(1, 2, 3)
