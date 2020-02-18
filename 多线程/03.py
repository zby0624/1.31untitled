'''
利用time延时函数，生成两个函数
利用多线程调用
计算总的运行时间
练习带参数的多线程启动方法
'''
import time
import _thread as thread

def loop1(in1):
    # ctime得到当前时间
    print("start loop1 at :",time.ctime())
    print("我是参数",in1)
    time.sleep(4)
    print("end loop1 at :",time.ctime())

def loop2(in1,in2):
     print("start loop2 at :",time.ctime())
     print("我是参数",in1,"我是参数",in2)
     time.sleep(2)
     print("end loop2 at :",time.ctime())

def main():
    print("start at:",time.ctime())
    # 启动多线程函数为start_new_thread
    # 参数两个，一个是需要运行的函数名，一个是函数的参数作为元组使用，为空则使用空元组
    # 注意！ 如果函数只有一个参数，则参数后面需要紧跟一个逗号
    thread.start_new_thread(loop1,("王老大，"))
    thread.start_new_thread(loop2,("王大鹏","王晓鹏"))
    print("all done at:",time.ctime())

if __name__ =='__main__':
    main()
    # 一定要有while语句
    # 因为启动多线程后，本程序就会作为主线程存在
    # 如果主线程执行完毕，那么子线程可能也需要终止
    while True:
        time.sleep(10)