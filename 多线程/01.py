'''
利用time生成两个函数
顺序调用
计算总的运行时间
'''
import time
def loop1():
    # ctime得到当前时间
    print("start loop1 at :",time.ctime())
    time.sleep(4)
    print("end loop1 at :",time.ctime())

def loop2():
     print("start loop2 at :",time.ctime())
     time.sleep(2)
     print("end loop2 at :",time.ctime())

def main():
    print("start at:",time.ctime())
    loop1()
    loop2()
    print("all done at:",time.ctime())

if __name__ =='__main__':
    main()