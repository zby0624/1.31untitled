# 全局解释锁 GIL
- https://www.cnblogs.com/jokerbj/p/7460260.html
- https://www.dabeaz.com/python/UnderstandingGIL.pdf

# 多线程 vs 多进程
- 程序：一堆代码以文本形式放入一个文档
- 进程：程序运行的一个状态
      - 包含地址空间，内存，数据栈等
      - 每个进程由自己完全独立的运行环境，多进程共享数据是一个问题
- 线程：一个进程的独立运行片段，一个进程可以有多个线程
      - 轻量化的进程
      - 一个进程的多个线程间共享数据和上下文运行环境
      - 共享互斥问题
- 多线程的作用是缩短运行时间，使运行的更快
- 全局解释锁(GIL)
      - python代码的执行是由python虚拟机进行控制
      - 在主循环中，只有一个控制线程在执行 
      
- python包
      - thread：有问题，不好用。python中改成_thread
      - threading：通行的包
      - 案例01.py: 顺序执行，耗时较长
        和 02.py ：改用多线程，缩短总时间，使用——thread
        03.py: 多线程，传参数
        
- threading的使用
      - 直接利用threading.Thread生成Thread实例
        1. t = threading.Tread(target=xxx, args=(xxx,))
        2. t.start():启动多线程
        3. t.join():等待多线程执行完成
        4. 案例04.py  t.join()是等待子线程执行完毕，print的语句最后执行
        - 守护线程 daemon
             - 如果在程序中，将子线程设置成守护线程，则子线程就会在主线程结束的时候自动退出
             - 一般认为，守护线程不可以离开主线程独立运行
             - 守护线程案例能否有效跟环境相关
      - 线程的常用属性
         - threading.currentThread:返回当前线程变量
         - threading.enumerate:返回一个正在运行的线程的list，正在运行的线程指的是线程启动或，结束前
         - threading.activeCount:返回正在运行的线程数量，效果跟len(threading.enumerate)一致
         - thr.setName:给线程设置名字
         - thr.getName:得到线程的名字
         
      - 直接继承自threading.Thread
         - 直接继承Thread
         - 重写run函数
         - 类实例可以直接运行
         - 案例05.py
 
- 共享变量
      - 共享变量：当多个线程同时访问同一个变量的时候，会产生共享变量的问题
      - 案例06.py
      - 解决共享变量问题：锁，信号灯
      - 锁(lock)
            - 是一个标志，表示一个线程在占用一个资源
            - 使用方法
                 - 上锁
                 - 使用共享资源，放心的用
                 - 取消锁（释放锁）
            - 案例07.py
            - 锁谁：哪个资源需要多个线程共享，就锁哪个
            - 理解锁：锁其实不是锁住谁，而是一个令牌
      - 线程安全问题：
            - 如果一个资源/变量，它对于多线程来讲，不用加锁也不会引起任何问题，则称为线程安全问题
            - 线程不安全变量类型：list,set,dict
            - 线程安全变量类型：queue(队列)
            
      - 生产者消费者问题：
           - 一个模型，可以用来搭建消息队列
           - queue是一个用来存放变量的数据结构，特点是先进先出，内部元素排队，可以理解成一个特殊的list
           - 案例08.py
      - 死锁问题
      - 锁的等待时间问题
      - semaphore
          - 允许一个资源最多由几个多线程同时使用
          - 案例09.py
      - threading.timer
          - Timer是利用多线程，在指定时间后启动一个功能
          - 案例10.py
          
      - 可重入锁
           - 一个锁，可以被一个线程多次申请
           - 主要是解决递归调用时候，需要申请锁的情况
           - 案例11.py
           
# 线程替代方案
- subprocess
      - 完全跳过线程，使用进程
      - 是派生进程的主要替代方案
      - python2.4后引用
- multiprocessing
      - 使用threading接口派生，使用子进程
      - 允许为多核或者多cpu派生进程，接口跟threading非常相似
      - python2.6后引用    
- concurrent.futures
      - 新的异步执行模块
      - 任务级别的操作
      - python3.2后引用
# 多进程
- 进程间通信(interprocesscommunication,IPC)
- 进程之间无任何共享问题
- 进程的创建
     - 直接生成Process实例对象
     - 案例11.py
     - 派生子类
     - 案例12.py
     
- 在os中可以查看pid(process id),ppid(parent process id)以及他们的关系
      - 案例13.py
      
- 生产者消费者模型   
      