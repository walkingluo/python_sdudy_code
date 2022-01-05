# -*- coding:utf-8 -*-

class Stack:
    '''
        stack
    '''
    def __init__(self):
        self.stack = []
    
    def __str__(self):
        return '|'.join(str(i) for i in self.stack)

    def push_value(self, value):
        self.stack.append(value)

    def pop_value(self):
        if self.stack:
            return self.stack.pop()
        else:
            return 'stack is empty'


if __name__ == '__main__':
    stack = Stack()

    stack.push_value(1)
    stack.push_value(2)
    stack.push_value(3)

    print(stack)

    print(stack.pop_value())
    print(stack.pop_value())
    print(stack.pop_value())
    print(stack.pop_value())

    print(stack)

