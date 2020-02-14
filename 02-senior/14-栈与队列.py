# 栈是一种容器可以存入、访问、删除数据元素，只能在一端存入或读取
# 栈没有位置概念，任何时候可以访问或删除的元素都是此前存入的最后一个元素
# （LIFO last in first out）先进后出

# 队列是一端存入，另一端读取
# （FIFO first in first out）先进先出

# 栈的实现
class Stack:
    """栈"""
    def __init__(self):
        self.__list = []
    def push(self,item):
        """添加一个新元素到栈顶"""
        self.__list.append(item)
    def pop(self):
        """弹出栈顶元素"""
        return self.__list.pop()
    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None
    def is_empty(self):
        """判断栈是否为空"""
        if self.size() == 0:
            return True
        else:
            return False
    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)


# 队列的实现
class Queue:
    """队列"""
    def __init__(self):
        self.__list = []
    def enqueue(self,item):
        """往队列中添加一个元素"""
        self.__list.append(item)
    def dequeue(self):
        """从队列头删除一个元素"""
        return self.__list.pop(0)
    def is_empty(self):
        """判断队列是否为空"""
        if not self.__list:
            return True
    def size(self):
        """返回队列长度"""
        return len(self.__list)

# 双端队列即首尾两个栈合在一起，在头部放入取出、在尾部放入取出
