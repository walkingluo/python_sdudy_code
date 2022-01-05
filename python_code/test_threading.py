# -*- coding:utf-8 -*-
# 多线程 对CPU密集型不利，IO密集型有利

import threading
import time

def start():

    i = 0
    for j in range(10000000):
        i += j
    return
    
def main():

    ts = {}
    s = time.time()
    for i in range(10):
        #start()
        t = threading.Thread(target=start)
        t.start()
        ts[i] = t
    for i in range(10):
        ts[i].join()  # 阻塞线程，使所有线程执行完毕，再继续主线程

    print(time.time()-s)

# 8.16722822189331  单线程运行10次start()
# 7.964332342147827 多线程运行，CPU密集型，GIL锁限制只能一个一个线程执行

number = 0
lock = threading.Lock()

def add_num():

    global number
    for i in range(1000000):
        lock.acquire()
        number += 1
        lock.release()

def dec_num():

    global number
    for i in range(1000000):
        lock.acquire()
        number -= 1
        lock.release()

def run_threading():

    global number
    t1 = threading.Thread(target=add_num)
    t2 = threading.Thread(target=dec_num)
    print("--start--")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(number)
    print("--stop--")


if __name__ == '__main__':

    #main()
    run_threading()