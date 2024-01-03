


class Demo :
    #fun()
    print("Start Class")
    def __init__(self):
        print("In constructor")

    def __del__(self):
        print("In Destructor")

    print("End Class")
print("Start Code")
obj = Demo()
obj1 = Demo()
obj2 = obj1
#del obj1
print("End Code")



