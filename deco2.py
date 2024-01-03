






def outerfun():
    print("In outer function")

    def innerfun1():
        print("In inner function1")

    def innerfun2():
        print("In inner function2")

    return innerfun1,innerfun2;



ret = outerfun()

ret[0]()
ret[1]()

