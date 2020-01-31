'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    # 定义一个空类，pass表示直接跳过
    pass

# 定义一个对象
mingyue = Student()

# 再定义一个类，用来表示学python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "python"

    # 需要注意的是：
    # 1. def dohomework的缩进层级
    # 2. 系统默认有一个self参数
    def dohomework(self):
        print("在做作业")

        # 推荐在函数末尾使用return语句
        return None

# 实例化一个叫yueyue的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 需要注意的是成员函数的调用，没有传递进去参数
yueyue.dohomework()

