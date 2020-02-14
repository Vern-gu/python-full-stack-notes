from distutils.core import setup

setup(name = "Vern", version = "1.0", description = "Vern's module",
author = "Vern", py_modules = ['sub.aa', 'sub.bb', 'sub.cc', 'sub.dd'])
# py_modules即包中的文件名
print(setup)

# 这个文件就是python包的安装文件
# 在python包的外部创建一个setup.py的文件后此文件夹就是一个python程序的安装包
# python3 setup.py build  # 运行这个文件
# python3 setup.py sdist  # 将安装文件压缩打包
