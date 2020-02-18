'''
- Server端流程
          1.建立socket，socket是负责具体通信的实例
          2.绑定，为创建的socket指派固定的端口和IP地址
          3.接受对方发送内容
          4.给对方发送给反馈，此步骤为非必须步骤
'''
# 建立socket模块
import socket

# 模拟服务器的函数
def serverFunc():
    # 1. 建立socket
    # socket.AF_INET:使用IPv4协议族
    # socket.SOCK_DGRAM:使用UDP协议
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定ip和port
    # 127.0.0.1:这个IP地址代表的是机器本身
    # 7852：随机指定的端口号
    # IP地址是一个tuple类型（IP，port）
    addr = ("127.0.0.1",7852)
    sock.bind(addr)

    # 3.接受访问
    # 等待方式为死等，没有其他可能性
    # recvfrom接收的返回值是一个tuple，前一项表示数据，后一项表示地址
    # 参数的含义是缓冲区大小
    data, addr = sock.recvfrom(500)

    print(data)
    print(type(data))

    # 发送过来的数据是bytes格式，必须通过解码才能得到str格式内容
    # decode默认参数是utf8
    text = data.decode()
    print(text)
    print(type(text))

    # 给对方返回的消息
    rst = "wo bu e "

    # 发送的数据需要编码成bytes格式
    # 编码默认格式也是utf8
    data = rst.encode()
    sock.sendto(data, addr)

if __name__ == '__main__':
    while True:
        try:
          serverFunc()
        except Exception as e:
            print(e)