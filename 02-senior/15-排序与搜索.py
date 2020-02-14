# 排序算法的稳定性：排序后使原本相等键值的的记录保持原来顺序即稳定，否则不稳定
# 冒泡排序：稳定
def bubble_sort(list):
    """冒泡排序"""
    n = len(list)
    for j in range(n-1):
        count = 0
        for i in range(n-1-j):  # 不用(n-1-j)则在外循环内需添加n-=1
            if li[i] > li[i+1]:
                li[i],li[i+1] = li[i+1],li[i]
                count += 1
        # n -= 1
        if 0 == count:
            return


# li = [12,4,5,13,0,6,23,11,10,56,64,2,7,14,1]
# bubble_sort(li)
# print(li)


# 选择排序：不稳定
def select_sort(list):
    """选择排序"""
    n = len(list)
    for i in range(n-1):  # 依次取出一个数与后半部分比较，小的放在前面
        for j in range(i+1,n):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]


# li2 = [12,4,5,1]
# select_sort(li2)
# print(li2)


# 插入算法：稳定
def insert_sort(list):
    """插入排序"""
    n = len(list)
    for i in range(1,n):  # 从后半无序部分取出数和前半部分有序数比较,小的插入其中
        for j in range(i,0,-1):
            if list[j] < list[j-1]:
                list[j],list[j-1] = list[j-1],list[j]
            else:
                break


# li3 = [12,4,5,13,0,6,2,1]
# insert_sort(li3)
# print(li3)


# 希尔排序：插入排序的变种，不稳定
def shell_sort(list):
    """希尔排序"""
    n = len(list)
    gap = n // 2
    while gap > 0:
        for j in range(gap,n):
            i = j
            while i > 0:
                if list[i] < list[i-gap]:
                    list[i],list[i-gap] = list[i-gap], list[i]
                    i -= gap
                else:
                    break
        gap //= 2


# 快速排序：不稳定（应用最广泛）
def quick_sort(list,first,last):  # 通过一趟趟排序，将列表分为两部分，其中一部分的元素要比另一部分元素都要小
    """快速排序"""
    if first >= last:
        return
    mid = list[0]
    low = first
    high = last
    while low < high:
        while low < high and list[high] >= mid:
            high -= 1
        list[low] = list[high]
        while low < high and list[low] < mid:
            low += 1
        list[high] = list[low]

    list[low] = mid            # 递归
    quick_sort(list,first,low-1)  # 对low左边列表继续快排
    quick_sort(list,low+1,last)  # 对low右边列表快排


def quick_sort2(li):
    if len(li)<2:
        return li
    m=li[0]
    low=[]
    high=[]
    mid=[]
    for i in li:
        if i<m:
            low.append(i)
        elif i==m:
            mid.append(i)
        else:
            high.append(i)
    return quick_sort2(low)+mid+quick_sort2(high)


# 归并排序：稳定
def merge_sort(list):
    n = len(list)
    if n <= 1:
        return list
    mid = n // 2
    left_li = merge_sort(list[:mid])  # 先用递归特性不断拆分列表
    right_li = merge_sort(list[mid:])
    left_pointer, right_pointer = 0,0
    result = []
    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1
            # 只要左右有一个列表遍历完就退出循环
    result += left_li[left_pointer]
    result += right_li[right_pointer]
    # 这时将另一边的列表剩下的部分加入
    return result


# 二分查找
def binary_search(list,item):  # 递归版本
    n = len(list)
    if n > 0:
        mid = n // 2
        if list[mid] == item:
            return True
        elif list[mid] > item:
            return binary_search(list[:mid],item)
        else:
            return binary_search(list[mid+1:],item)
    return False


def bin_search(list,item):  # 非递归
    n = len(list)
    first = 0
    last = n-1
    while first <= last:
        mid = (first+last)//2
        if list[mid] == item:
            return True
        elif item<list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    a=[1,24,5,6,8,3,234,12,445,123,521,35,6,1,2,34,23,45,34,124,56,899,22,12,56,16,95,24,67,89,63,24,123,36,89,2,57,9,34,46,7]
    print(quick_sort2(a))