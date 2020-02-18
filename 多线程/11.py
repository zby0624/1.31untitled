import multiprocessing
import time

def clock(interval):
    while True:
        print("the tie is %s" % time.ctime())
        time.sleep(interval)

if __name__ == '__main__':
    p = multiprocessing.Process(target = clock, args = (5,))
    p.start()

    while True:
        print("sleep.....")
        time.sleep(1)