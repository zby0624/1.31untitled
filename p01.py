# 包含一个类
# 一个sayhi函数
# 打印一句话

class Student():
    def __init__(self, name="noname", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("my name is {0}".format(self.name))

def sayhi():
    print("hi,欢迎")

# 此判断语句建议一直作为程序的入口
if __name__ == '__main__':
     print("我是模块p01")