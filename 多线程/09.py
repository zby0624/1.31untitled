import time
import threading

# semaphore参数定义 最多有几个多线程同时使用资源
semaphore = threading.Semaphore(3)

def func():
    if semaphore.acquire():
        for i in range(5):
            print(threading.currentThread().getName() + 'get semaphore')
        time.sleep(15)
        semaphore.release()
        print(threading.currentThread().getName() + 'release semaphore')

for i in range(8):   # 同时8个多线程在执行
    t1 = threading.Thread(target=func)
    t1.start()