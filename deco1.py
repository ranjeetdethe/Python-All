



def outerfun():
    print("In outer function")

    def innerfun1():
        print("In inner function")
    
    def innerfun2():
        print("In inner function 2")


    innerfun1()
    innerfun2()

outerfun()

