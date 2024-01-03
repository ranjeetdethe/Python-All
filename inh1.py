



class demo:

    def __init__(self):
        print("Constructor")
        self.x=10
        self.y=20

    def setdata(self,z):
        self.z=z

    def printdata(self):
        print(self.x)
        print(self.y)
        print(self.z)

obj1 = demo()
obj1.setdata(30)
obj1.printdata()
