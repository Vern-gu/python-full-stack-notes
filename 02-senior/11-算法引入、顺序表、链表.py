# 算法：
# 如果a+b+c = 1000，且a^2+b^2=c^2,(a，b，c为自然数),求出所有a，b，c

# for a in range(1001):  # 法一、枚举法
#     for b in range(1001):
#         for c in range(1001):
#             if a*a + b*b == c*c:
#                 if a+b+c == 1000:
#                     print(a,b,c)
# 运算数量为1000*1000*1000*2

for a in range(1001):  # 法二、稍作改进
    for b in range(1001):
        c = 1000 - a - b
        if a*a + b*b == c*c and a+b+c == 1000:
            print(a,b,c)
# 运算数量为1000*1000*3

# 可以用计算机的基本运算数量来衡量时间复杂度
# 算法完成工作最多需要的基本操作步骤，称为最坏时间复杂度；反之称为最优时间复杂度
# O(1)< O(logn)< O(n)< O(nlogn)< O(n^2)< O(n^2logn) < O(n^3)< O(2^n)< O(n!)< O(n^n)


import timeit  # 该模块用于测算代码的执行时间

# time1 = timeit.Timer('test1()','from __main__ import test1')
# time1.timeit(1000)  # 上面的程序测算1000次


# ==================================================================
# 数据结构：
# 顺序表：相同类型的数据放在一起存储时，其内存地址是连续的（包含表头，这片内存总共能放多少数据，已有多少数据）
# 而不同类型的数据存放在一起时，会给所有数据创建一个指向数据的“地址”，这些地址的内存空间都是连续的

# 链表：数据的存放是无序的，但是却被串联在一起，前一个数据中会有一片区域放入一个地址指向下一个数据
class Node(object):
    '''节点'''
    def __init__(self,elem):
        self.elem = elem
        self.next = None  # 指向下一个节点

class SingleLink(object):
    """单链表"""
    def __init__(self, node=None):
        self.__head = node  # 头节点
    def is_empty(self):
        """链表是否为空"""
        return self.__head is None  # 这条语句为判断(空则返回True)
    def length(self):
        """链表长度"""
        cur = self.__head  # cur用于遍历各个节点，相当于指针
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next  # node.next
        return count
    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        travel_list = []
        while cur is not None:
            travel_list.append(cur.elem)
            cur = cur.next
        print(travel_list)
    def add(self,elem):
        """链表头部添加元素"""
        node = Node(elem)
        node.next = self.__head
        self.__head = node
    def append(self,elem):
        """链表尾部添加元素"""
        node = Node(elem)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
    def insert(self,position,elem):  # 在指定位置中插入数据
        """链表中间添加元素"""
        if position <= 0:
            self.add(elem)
        elif position > (self.length()-1):
            self.append(elem)
        else:
            prior = self.__head  # prior前一位
            node = Node(elem)
            count = 0
            while count < (position-1):
                prior = prior.next
                count += 1  # 循环退出后，prior指向position-1位置
            node.next = prior.next  # 先让要插入数据的next指向prior.next
            prior.next = node  # 再将原来的断开，指向新的数据
    def search(self,elem):  # 存在就返回位置，不存在返回-1
        """查找节点是否存在"""
        cur = self.__head
        count = 0
        position = -1
        while cur is not None:
            if cur.elem == elem:
                position = count
                break
            count += 1
            cur = cur.next
        return position
    def remove(self,elem):
        """删除链表中元素"""
        prior = self.__head
        if self.search(elem) == 0:  # 判断要删除的数据是否为头节点
            self.__head = prior.next
        else:
            count = 0
            while prior is not None:
                if count == self.search(elem)-1:
                    prior.next = prior.next.next
                prior = prior.next
                count += 1


if __name__ == '__main__':
    item = Node(100)
    sll = SingleLink(item)
    sll.append(12)
    sll.add(10)
    sll.insert(1,120)
    sll.remove(12)
    sll.travel()

    print(sll.search(200))
    print(sll.length())