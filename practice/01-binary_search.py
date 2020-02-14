def binary_search(list,item):
    low = 0
    high = len(list)-1
    while low < high:
        mid = (low + high) // 2
        if list[mid] == item:
            return mid
        elif list[mid] > item:
            high = mid
        else:
            low = mid
    return mid


a = [1,3,4,5,6,9,7,6,9,0,2]
a.sort()
print(a)
b = binary_search(a,9)
print(b)