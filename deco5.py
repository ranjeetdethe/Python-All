  



# Decorartor functions

def decorfun(func):
    
    def wrapper():
        print("Start Wrapper")
        func()
        print("End Wrapper")

    return wrapper

@decorfun

def normalfun():
    print("In normal Function")

#normalfun = decorfun(normalfun)
normalfun()
