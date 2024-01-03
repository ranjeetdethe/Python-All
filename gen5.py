






def fun(x,y):
    print("Start")
    while(x<=y):
        yield x
        x=x+1

    print("End")

for val in fun(1,10):
    print(val)
    






    
