




def outer():
    def inner():
        return "Hello I'm in inner function"
    return inner
retobj = outer()
retinner = retobj()

print(retinner)
