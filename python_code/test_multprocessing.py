# -*- coding:utf-8 -*-
# 多进程

from multiprocessing import Process, Queue, Pool
from multiprocessing import current_process
import time

def start(i):

    time.sleep(1)
    print(i)
    print(current_process().name)
    print(current_process().pid)
    print(current_process().is_alive())

    return i

def write(q):
    
    print("process to write: {}".format(current_process().pid))
    for i in range(5):
        print("put {} into q".format(i))
        q.put(i)

def read(q):

    print("process to read: {}".format(current_process().pid))
    while True:
        value = q.get()
        print("get {} from queue".format(value))

def main():

    print("--start--")
    '''
    q = Queue()
    p1 = Process(target=write, args=(q,), name='p1')
    p2 = Process(target=read, args=(q,), name='p2')
    p1.start()
    p2.start()
    '''
    # 进程池
    pool = Pool(processes=4)
    pool_output = pool.apply(start, args=(1,))
    pool.close()
    pool.join()
    print(pool_output)
    print("--stop--")

if __name__ == '__main__':

    main()
