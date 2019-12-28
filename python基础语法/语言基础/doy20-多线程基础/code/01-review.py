"""__author__=桃花寓酒寓美人"""
from socket import socket
"""
服务器：
1.创建socket对象
2.绑定ip和端口  
3.准备监听
4.保证服务器一直运行
    1)接受请求
    2)接收消息
    3)发送消息
    4)关闭连接

客户端：
1.创建socket对象
2.建立连接
3.接受消息
4.发送消息
5.关闭连接
"""

server = socket()
server.bind(('', 12345))
server.listen(520)
while True:
    connection, address = server.accept()
    re_data = connection.recv(1024)
    print(re_data.decode())

    connection.send('你好'.encode())

