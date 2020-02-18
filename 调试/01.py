def sayhi(name):
    print("i want to say hi with {0}".format(name))
    print("hello,{0}".format(name))

if __name__ == "__main__":
    print('*' * 50)
    name = input("put your name here:")
    print(sayhi(name=name))
