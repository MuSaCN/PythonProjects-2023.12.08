# Author:Zhang Yuan

# ---注意：
# 1. 如果有读取文件时，要注意会出错。因为exe执行是在系统临时文件下，但是其下面没有文件，所以会导致错误。
# 2. 若存在动态的导入库，也会出错。所以打包为exe时，若要用到的方法有动态导入库，需要显式的导入。

# ---单exe文件
# pyinstaller -F __各种测试\\其他功能性测试\\python打包exe.py

# ---多文件
# pyinstaller -D __各种测试\\其他功能性测试\\python打包exe.py


a = input("输入你的内容：")
print(a)
b = input("再次输入你的内容：")
print(b)

