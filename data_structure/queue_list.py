# -*- coding:utf-8 -*-

class Queue:
    '''
        queue
    '''
    def __init__(self):
        self.queue = []

    def __str__(self):
        return '|'.join(str(i) for i in self.queue)

    def add(self, value):
        self.queue.append(value)

    def remove(self):
        return self.queue.pop(0)

    
if __name__ == '__main__':

    queue = Queue()

    queue.add(1)
    queue.add(2)
    queue.add(3)

    print(queue)

    print(queue.remove())

    print(queue)