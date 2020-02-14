print("==========多线程==========")
# 进程内会有线程来执行程序，多线程就是在进程不变的前提下（即不多占用内存），完成多任务
import time
from threading import Thread,Lock  # thread模块更为底层，threading是经过封装过的，推荐使用threading

def saySomething():
    print("life is fantastic")
    time.sleep(1)

for i in range(5):
    t = Thread(target=saySomething)
    t.start()
# 用Thread创建子线程的话，主线程会一直等到子线程结束才会结束
# 多个线程执行同一个函数的话，各自之间不会有影响，各管各的


print("==========Thread子类创建多线程==========")
class Test(Thread):  # 创建一个继承Thread的类
    def run(self):
        for i in range(3):
            print(self.name+" @ "+str(i))
            time.sleep(1)

t = Test()  # 同Process类一样，调用时会自动调用run方法
t.start()
# 线程共享全局变量
# 因此两个线程同时操作一个全局变量时可能会出错，即同步不及时
# 此时应当使一个线程先完成全局变量的操作，再让另一个线程操作(轮询、互斥锁)


print("==========互斥锁==========")
# 互斥锁保证了每次只有一个线程进行了写入操作，从而保证多线程情况下数据的正确性
g_num = 0
def plus1():
    global g_num
    mutex.acquire()  # 上锁，当有一个线程抢先执行了此步，则其他线程会堵塞
    for i in range(100000):
        g_num += 1
    mutex.release()  # 解锁，运行至这步时，其它堵塞的线程开始执行
    print("plus1,g_num = %d"%g_num)

def plus2():
    global g_num
    mutex.acquire()
    for i in range(100000):
        g_num += 1
    mutex.release()
    print("plus2,g_num = %d"%g_num)

mutex = Lock() # 创建一把互斥锁，默认是开锁状态
p1 = Thread(target=plus1)
p2 = Thread(target=plus2)
p1.start()
p2.start()

# 非全局变量，每个线程各自管各自的，不会共享数据
# 死锁：在线程间共享多个资源的时候，如果两个线程分别占有一部分资源并且等待对方的资源，就会造成死锁


print("==========同步==========")
# 同步是指协同步调，按约定的先后次序来运行
# 这里的“同”指的是协同、协助、互相配合，而不是一起动作
# 而异步就是将来谁先要执行是不确定的
'''
class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():  # 1号上锁
                print(1)
                time.sleep(0.5)
                lock2.release()  # 2号解锁

class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():  # 若2号可以上锁：
                print(2)
                time.sleep(0.5)
                lock3.release()

class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():
                print(3)
                time.sleep(0.5)
                lock1.release()

lock1 = Lock()
lock2 = Lock()
lock3 = Lock()
lock2.acquire()  # 2号上锁
lock3.acquire()  # 3号上锁
t1 = Task1()
t2 = Task2()
t3 = Task3()
t1.start()
t2.start()
t3.start()
'''

print("----------生产者与消费者模式----------")
# 这里的队列是线程中用的，与之前multiprocessing中的队列不同，不能混用，但两者用法相同
from queue import Queue
# 阻塞队列就是就是用来给生产者和消费者解耦的
class Producer(Thread):
    def run(self):
        global q
        count = 0
        while True:
            if q.qsize() < 1000:
                for i in range(100):
                    count += 1
                    msg = "生成产品 "+str(count)
                    q.put(msg)
                    print(msg)
            time.sleep(0.5)

class Consumer(Thread):
    def run(self):
        global q
        while True:
            if q.qsize() > 100:
                for i in range(10):
                    msg = self.name+" 消费了 "+q.get()
                    print(msg)
            time.sleep(1)

q = Queue()
for i in range(500):
    q.put("原料"+str(i))
for i in range(2):
    p = Producer()
    p.start()
for i in range(5):
    c = Consumer()
    c.start()


# ThreadLocal多线程全局传参，数据不会混用
print("==========threading.local()==========")
# 使用时创建一个全局的ThreadLocal对象
import threading
g_local = threading.local()

def process():
    g_local.aa = "asd"  # 为这个对象添加属性，将要传递的参数添加进这个属性中
# 然后传递local对象中的属性即可传递参数
# threading.local()这个方法的特点用来保存一个全局变量，但是这个全局变量只有在当前线程才能访问




print("==========异步==========")
from multiprocessing import Pool
import time
import os

def test():
    print("进程池中的进成为pid = %d, ppid = %d"%(os.getpid(),os.getppid()))
    for i in range(3):
        print("---i---")
        time.sleep(1)
        return "子进程返回值"

def test2(args):
    print("主进程pid = %d"%os.getpid())
    print("接收  %s"%args)

p = Pool(3)
p.apply_async(func=test,callback=test2)
# 加入callback参数后，当子进程的任务完成后会让主进程立即执行callback任务，并将子进程返回的值传给主进程
time.sleep(10)
print("主进程pid = %d"%os.getpid())


# 多进程的效率远大于线程
# 在python中会存在一个GIL的问题
# 即使用多线程时，多核cpu其实并不能满负荷运行
# 这时可以让python的某个线程运行c语言写的代码
# 可以提高cpu使用效率，即关键部位用c语言重写，再在python中导入即可
