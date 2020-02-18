import multiprocessing
import time

class ClockProcess(multiprocessing.Process):
    # 跟案例05.py类似
    def __init__(self,interval):
        self.interval = interval
        super(ClockProcess,self).__init__()

    def run(self):
        while True:
            print("the time is %s" % time.ctime())
            time.sleep(self.interval)

if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()
    
    while True:
       time.sleep(1)