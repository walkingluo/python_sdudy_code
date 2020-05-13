# -*- coding:utf-8 -*-
import datetime
import time
from functools import wraps


def logger(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        strat = datetime.datetime.now()
        res = fn(*args, **kwargs)
        run_time = (datetime.datetime.now() - strat).total_seconds()
        print(fn.__name__, run_time)
        return res
    return wrapper


@logger
def add_num(x, y, z=3):
    time.sleep(1)
    s = x + y + z
    print(s)
    return s


# add_num(1,2)
'''
def generator():
    for i in range(5):
        yield i

print(next(generator()))

for i in generator():
    print(i)
'''
x = "abc"
y = "def"
m = x.join(y)
print(m)
