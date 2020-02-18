import json

# 此时student是一个dict格式内容，不是json
student = {
    "name":"liudana",
    "age":19,
    "mobile":"878548752"
}

print(type(student))

stu_json = json.dumps(student)
print(type(stu_json))
print("json对象{0}".format(stu_json))

stu_dict = json.loads(stu_json)
print(type(stu_dict))
print(stu_dict)