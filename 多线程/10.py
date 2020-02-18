import time
import threading

def func():
    print("i am running ....")
    time.sleep(4)
    print("i am done ....")

if __name__ == '__main__':
    t = threading.Timer(6, func)   # 表示6秒之后执行函数
    t.start()

    i = 0
    while True:
        print("{0} --------",format(i))
        time.sleep(3)
        i += 1