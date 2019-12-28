"""__author__=桃花寓酒寓美人"""

# 1.数据的存储
"""
1）数据存储的特点
计算机中的内存分为硬盘和运行内存；
硬盘是用来存储文件的，除非手动删除过着硬盘出现问题，否则存储在硬盘中的文件一直存在不会销毁；
运行内存是用来存储，程序在运行过程中产生的数据；当程序运行结束后会自动销毁

如果希望程序中产生的数据在程序运行结束后不销毁，就需要将数据存储到硬盘中

2）常用的文件
txt文件、json文件、plist文件、数据库文件等 - - 文本数据
图片文件(png，jpg等)、音频文件(mp3，wav)、视频文件... -- 二进制文件
"""

# 2.文件操作1：操作文件内容
"""
1) 文件操作基本步骤
打开文件 -> 操作文件(读、写) -> 关闭文件
"""
# 2.1 打开文件
"""
open(file, mode='r',...,encoding=None)
open(文件路径，打开方式，文本编码方式) - 以指定的方式打开指定文件并且返回文件对象

说明：
file - 文件路径；可以传文件的绝对路径和相对路径
        1）绝对路径：文件的完整地址
        2）相对路径：./  - 表示当前目录
                     ../ - 表示当前目录的上层目录

mode  - 文件打开方式，决定打开文件后的操作权限(读写);
        操作文件的时候数据的类型（文件/二进制 - t/b）
        r - 只读； w - 只写；a - 只写；t - 文本数据(默认)；b - 二进制
        r(rt/tr) - 打开文件后只能进行读操作，读出来数据是字符串
        rb/br    - 打开文件后只能进行读操作，读出来的数据是二进制(bytes)
        w(wt/tw) - 打开文件后只能进行写操作，写入的数据是字符串；打开的时候清空原文件
        wb/bw    - 打开文件后只能进行写操作，写入的数据是二进制；打开的时候清空原文件
        a(at/ta) - 打开文件后只能进行写操作，写入的数据是字符串；打开的时候不会清空原文件
        ab/ba    - 打开文件后只能进行写操作，写入的数据是二进制；打开的时候不会清空原文件
        
        注意：a、w在打开文件的时候，如果文件不存在，会自动创建文件
              r在打开文件的时候，如果文件不存在，会报错
              
encoding - 文本文件编码方式；只能以t的方式打开文本文件的时候可以赋值
         - 一般采用"utf-8"的编码方式进行编码；保证同一文件读写方式一致

"""
# ====================== 1.文件路径 ========================
# open(r'D:\知识学习类\Python\project_xm\python1906\02-语言基础\day13-文件操作和异常捕获\code\test_txt.txt')
# txt = open(r'test_txt.txt')
# print(txt)

# ====================== 2.打开方式 ========================
# open('test_txt.txt', 'w')
# a = open('test_txt.txt', encoding='utf-8')
# print(a.read())

# 2.2操作文件
"""
1) 读操作
文件对象.read() - 读指定文件，并且返回文件中的内容(所有的文件都支持)
文件对象.readline() - 读指定文件一行的内容(只支持文本文件)

2) 写操作
"""
# f = open('test.txt', 'r', encoding='utf-8')
# 读一行
# print(f.readline())
# 读剩下
# print(f.read(), '\n')
# 光标操作; 文件对象.seek(N) - 将读写位置移动到第N个字节的位置
# f.seek(0)  # 将光标移动到文件开头
# print(f.read())
# f.close()

# 练习：都指定文本文件中的内容，一行一行的读，读完为止
# f = open('test.txt', 'r', encoding='utf-8')
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         break
# f.close()

# 文本文件打开方式带b，读出来的数据是二进制数据
# f = open('test.txt', 'rb')
# content = f.read()
# print(content, type(content))
# f.close()

# 注意：二进制文件(图片、音频、视频、exe文件等)打开时时候必须带b

# 2.3写操作
"""
文件对象.write(内容) - 将指定的内容写入到指定文件中
"""
f = open('test.txt', 'a', encoding='utf-8')
f.write('and')
str_utf8 = 'hello'.encode('utf-8')
print(str_utf8)


