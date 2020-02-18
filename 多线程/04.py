import time
import threading

def loop1(in1):
    # ctime得到当前时间
    print('start loop1 at :', time.ctime())
    print("我是参数",in1)
    time.sleep(4)
    print('end loop1 at :',time.ctime())

def loop2(in1,in2):
     print('start loop2 at :',time.ctime())
     print("我是参数" , in1,"我是参数" , in2)
     time.sleep(2)
     print('end loop2 at :',time.ctime())

def main():
    print('start at:',time.ctime())
    # 生成threading实例
    t1 = threading.Thread(target=loop1 ,args=("王大拿，"))
    t1.start()

    t2 = threading.Thread(target=loop2 , args=("王大鹏，王晓鹏"))
    t2.start()
    t1.join()
    t2.join()
    print("all end at:",time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)