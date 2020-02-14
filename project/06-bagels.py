import random


a = str(random.randint(0,9))
b = str(random.randint(0,9))
c = str(random.randint(0,9))
l = [a,b,c]
# print(l)
k = 0

while k < 5:
    k += 1
    s = input("enter 3 numbers:(separate by commas)")
    l2 = s.split(",")
    # print(l2)
    for i in range(len(l2)):
        if l2[i] not in l:
            print("Bagels",end=' ')  # 不存在该数字
        else:
            if l2[i] == l[i]:
                print("Fermi",end=' ')  # 数字正确
            else:
                print("Pico",end=' ')  # 数字存在但位置不对
        print("")
    if l2 == l:
        print("You Win!")
        break
if k >= 5:
    print("You lose")
