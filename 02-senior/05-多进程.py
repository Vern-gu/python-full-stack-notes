print("=========调试程序 pdb========")
# 1.执行时调试：python3 -m pdb 文件名.py
# l：显示源代码、n：向下执行一行代码、c：继续执行代码（该停就停，不停就不停） \
# b (行数)：添加断点、clear (序号)：删除断点、s：(执行到函数调用时)进入该函数 \
# p (形参)：(在函数内)查看传递给函数的该参数的值、a：直接查看所有参数的值 \
# q：退出调试、r：(在函数内)快速执行到函数的最后一行

# 2.交互调试：（进入python解释器）import pdb \
# pdb.run("函数名(args)")  # 先使用s跳转到这个testfun函数中，然后就可以使用

# 3.程序里埋点：当程序执行到pdb.set_trace()位置时会停下调试


print("==============多任务=============")
# 并发：少核心运行多个任务；并行：多个核心同时运行多个任务
# 调度算法：时间片轮转、优先级调度（并发）
# 编写完毕的代码，没有运行时称之为程序；运行中的程序称之为进程，进程除了包含代码还需要运行的环境

# 在python中用fork()函数添加子进程，以实现多任务
'''
import os
# fork函数只能在unix/Linux/Mac上运行，Windows不行
pid = os.fork()  # 运行到这步时，fork函数会创建一个子进程
if pid == 0:
    print("子进程")
else:
    print("主进程")
print("over")  # over会被执行两次
'''
# os.getpid()  获取当前进程的序号
# os.getppid()  获取当前进程的父进程的序号
# 一般fork函数会返回一个0和一个大于0的值，而大于0的值就是生成的子进程的序号
# 所有变量，无论全局或局部，在各自的进程中都互不干扰

# windows中使用multiprocessing模块来使用多进程
'''
from multiprocessing import Process
import time

def test(name):
    for i in range(5):
        print("---%s---"%name)
        time.sleep(1)

p = Process(target=test,args=("test",))  # 新建了一个进程指向test函数，并为其传递参数
p.start()  # 让这个进程开始执行test函数里的代码
p.join()  # (堵塞([timrout]))该函数可以让子进程(p)先运行，在其结束后才运行主进程
for i in range(3):
    print("---main---")
    time.sleep(1)
'''
# 通过process创建子进程的话，主进程会一直等待子进程全部结束后才会结束


# Process子类创建进程
'''
class ProcessClass(Process):
    def __init__(self,interval):
        # Process本身也有init方法，但我们并没有完全重写这个方法，因此需要调用父类的init
        Process.__init__(self)  # 一定要用Process.__init__(self)
        self.interval = interval
    def run(self):  # 重写Process的run方法
        print("子类start")
        tStart = time.time()
        time.sleep(self.interval)
        tStop = time.time()
        print("子类over%0.2f"%(tStart-tStop))  # %.2f 是指该浮点型float数值保留两位小数


p = ProcessClass(2)  # 只要调用了Process类的对象就一定会执行run方法
p.start()
p.join()
print("结束")
'''

print("==============进程池 Pool=============")
from multiprocessing import Pool
import os

def worker(num):
    for i in range(5):
        print("pid = %d   num = %d"%(os.getpid(),num))

po = Pool(3)  # 表示进程池中最多有三个进程同时执行
for i in range(10):
    po.apply_async(worker,(i,))  # 向进程池中添加任务和参数
    # po.apply()  堵塞式添加任务，只有上一个任务完成后才能再添加任务，无视Pool(3)
# 如果添加的任务超过了同时执行的进程数，则多余的任务会等待其他任务完成后自动加入进程池
po.close()  # 关闭进程池，相当于不能再添加新任务
po.join()  # 默认情况下主进程并不会等待子进程完成后再结束


print("=============队列Queue===========")
# 队列：先进先出
# 栈：先进后出
from multiprocessing import Queue, Process
import os, time, random
'''
q = Queue(3)  # 初始化一个Queue对象，最多可接受3条put消息
q.put("message1")  # put,往队列中添加消息，消息的类型可以是任意的
q.put("message2")
q.qsize()  # 查看队列中有多少消息
# 如果添加的消息超过了队列的容量，继续添加时队列会堵塞，即会等到队列有空位置时再会自动添加新的消息
q.get()  # 取出队列中最先添加的消息
q.empty()  # 如果队列为空则返回True，否则返回False
q.full()  # 如果队列满了则返回True，否则返回False
'''
def write(q):
    for i in range(5):
        print("appending...")
        q.put(i)
        time.sleep(random.random())

def read(q):
    while True:
        if not q.empty():
            print(q.get())
            time.sleep(random.random())
        else:
            print("empty")
            break


q = Queue()  # 没有填参数，则队列的容量可以无限大
pw = Process(target=write,args=(q,))
pr = Process(target=read,args=(q,))
pw.start()
pw.join()  # pw.join写在前面，则pw先执行完毕才会执行pr
pr.start()
pr.join()
print("OVER")

# 在进程池中Pool使用队列的话需要在multiprocessing中导入Manager
# 使用Manager().Queue()来创建队列


print("=========多进程拷贝文件=========")
