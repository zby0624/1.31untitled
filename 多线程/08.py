import threading
import time
import queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            # queue.size返回的是queue内容的长度
            if queue.qsize() < 1000:
                for i in range(1000):
                    count += 1
                    mrg = '生成商品' + str(count)
                    # queue.put是往queue中放入值
                    queue.put(mrg)
                    print(mrg)
            time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(3):
                    # get从queue中拿出一个值
                    mrg = self.name + '消费' + queue.get()
                    print(mrg)
            time.sleep(1)

if __name__ == '__main__':
    queue = queue.Queue()

    for i in range(500):
        queue.put('初始产品' + str(i))

    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()