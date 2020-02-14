# 单项循环链表
class Node:
    def __init__(self,item):
        self.elem = item
        self.next = None


class SingleCycleLinkList:
    def __init__(self,node=None):
        self.__head = node
        if node:
            node.next = node
    def is_empty(self):
        return self.__head is None
    def length(self):
        if self.is_empty():
            return 0
        cur = self.__head
        count = 1
        while cur.next != self.__head:
            count += 1
            cur = cur.next
        return count
    def travel(self):
        if self.is_empty():
            return
        cur = self.__head
        print("[",end='')
        while cur.next != self.__head:
            print(cur.elem,end=' ')
            cur = cur.next
        print(str(cur.elem) + "]")  # 循环结束后cur指向尾节点，但尾节点未打印
    def add(self,item):
        """链表头部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        cur = self.__head
        while cur.next != self.__head:
            cur = cur.next
        node.next = self.__head
        self.__head = node
        cur.next = node
    def append(self,item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = cur.next
            cur.next = node
    def insert(self,position,item):  # 在指定位置中插入数据
        """链表中间添加元素"""
        if position <= 0:
            self.add(item)
        elif position > (self.length()-1):
            self.append(item)
        else:
            prior = self.__head  # prior前一位
            node = Node(item)
            count = 0
            while count < (position-1):
                prior = prior.next
                count += 1  # 循环退出后，prior指向position-1位置
            node.next = prior.next  # 先让要插入数据的next指向prior.next
            prior.next = node  # 再将原来的断开，指向新的数据
    def search(self,item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self.__head
        while cur.next != self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        if cur.elem == item:
            return True
        return False
    def remove(self,item):
        """删除链表中元素"""
        if self.is_empty():
            return
        cur = self.__head
        pre = None
        while cur.next != self.__head:
            if cur.elem == item:
                if cur == self.__head:  # 判断是否为头节点
                    rear = self.__head
                    while rear.next != self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head
                else:
                    # 中间的节点
                    pre.next = self.__head
                return
            else:
                pre = cur
                cur = cur.next
        if cur.elem == item:  # 退出循环cur指向尾节点
            if cur == self.__head:
                # 链表只有一个节点
                self.__head = None
            else:
                pre.next = cur.next


elem = Node(12)
scll = SingleCycleLinkList()
scll.travel()

