# 欧几里得算法：一种得出两个整数的最小公约数的方法
# gcd(a,b) = gcd(b,a mod b)  (设a>b 且r=a mod b ,r不为0)


# 使用D&C解决问题的过程包括两个步骤（递归）：
# (1) 找出基线条件，这种条件必须尽可能简单。
# (2) 不断将问题分解（或者说缩小规模），直到符合基线条件。


def sum(arr):  # 用递归的方式将列表中的数字相加
    # if 0 == len(arr):
    #     return 0
    # else:
    #     return arr.pop()+sum(arr)
    if arr == []:
        return 0
    return arr[0]+sum(arr[1:])


def count(arr):  # 用递归的方式计算列表包含的元素数量
    if arr == []:
        return 0
    return 1+count(arr[1:])


def max(arr):  # 用递归方式求出列表内最大元素
    if 2 == len(arr):
        return arr[0] if arr[0] > arr[1] else arr[1]
    m = max(arr[1:])
    return arr[0] if arr[0] > m else m


def quick_sort(arr):  # 快速排序
    if len(arr) < 2:  # 基线条件
        return arr
    less = []
    greater = []
    equal = []
    for i in arr:
        if i > arr[0]:
            greater.append(i)
        elif i < arr[0]:
            less.append(i)
        else:
            equal.append(i)
    return quick_sort(less)+equal+quick_sort(greater)  # 将大小两部分再分别使用快排


print(sum([1,2,3,4,5]))
print(count([1,2,3,4,5]))
print(max([1,2,3,4,5,6]))
print(quick_sort([12,4,53,23,2,56,11,7,32,1,21,13]))