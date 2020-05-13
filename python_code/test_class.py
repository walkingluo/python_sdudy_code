def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

# recurse(0, 0)


class Student():
    def __getattr__(self, attr):          # 定义当获取类的属性时的返回值
        if attr == 'age':
            return 25                     # 当获取age属性时返回25
        raise AttributeError('object has no attribute: %s' % attr)

    def __len__(self):
        print(self)
        return 5


'''
s = Student()
print(s.age)
print(s.name)
print(len(s))
print(len(Student))
'''


class MyDict(dict):
    def __setitem__(self, key, value):                 # 该函数不做任何改动 这里只是为了输出
        print('setitem:', key, value, self)
        super().__setitem__(key, value)

    def __getitem__(self, item):                       # 主要技巧在该函数
        print('getitem:', item, self)                  # 输出信息
                                                       # 基本思路: a[1][2]赋值时 需要先取出a[1] 然后给a[1]的[2]赋值
        if item not in self:                           # 如果a[1]不存在 则需要新建一个dict 并使得a[1] = dict
            temp = MyDict()                            # 新建的dict: temp
            super().__setitem__(item, temp)            # 赋值a[1] = temp
            return temp                                # 返回temp 使得temp[2] = value有效
        return super().__getitem__(item)


'''
test = MyDict()
test[0] = 'test'
print(test[0])
test[1][2] = 'test1'
print(test[1][2])
test[1][3] = 'test2'
print(test[1][3])
'''


class ArrayList:
    def __init__(self, number_list):
        self.numbers = number_list

    def __iter__(self):
        self.pos = 0
        return self

    def __next__(self):
        if(self.pos < len(self.numbers)):
            self.pos += 1
            return self.numbers[self.pos - 1]
        else:
            raise StopIteration


'''
array_obj = ArrayList([1, 2, 3])
it = iter(array_obj)
print(next(it))
print(next(it))
'''


class Developer:
    coffee_cups = 0

    def __init__(self, name):
        self.name = name
        self.coffee_cups += 1

    def speak(self):
        print(f"I'm {self.name} and I've had {self.coffee_cups} cups of coffee today")


'''
rover = Developer("Steve")
print(rover.coffee_cups)
rover.speak()
spot = Developer("Bob")
print(spot.coffee_cups)
spot.speak()
'''


class parent:
    def __init__(self, param):
        self.v1 = param


class child(parent):
    def __init__(self, param):
        super(child, self).__init__(param)
        self.v2 = param


'''
obj = child("11")
print(obj.v1 + " " + obj.v2)
'''


class Person:
    def __init__(self, name):
        __name__ = name
        print(__name__)

    def getAge(self):
        print(__name__)


'''
p = Person("John")
p.getAge()
'''


x = 9


def fn():
    y = 3
    z = y + x
    globals()['x'] = 3
    # Calling the globals() method
    # z = globals()['x']
    return z, x


ret = fn()
print(ret)
