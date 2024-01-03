


class Parent :
    def __init__(asd):
        print("In constructor Parent")

    def parentfunc(asd):
        print("In Parent function")

class child(Parent):
    print("In child consstructor")


obj1 = child()
obj1.parentfunc()
