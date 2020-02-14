# 给程序传递参数
import sys
def a(num):
    print(num)
def b(num):
    print(num)
    a(100)

print(sys.argv) # 值为["xxx.py"]

if sys.argv[1] == a:  # 这里的a就是外部给程序传递的参数
    b(12)

# 交互模式下用python3 xxx.py 参数（多个参数空格隔开）
# 所传递的参数会保存在sys.argv这个列表中

