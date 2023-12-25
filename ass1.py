


def outer():
    def inner():
        return "Hello I'm inner function"
    return inner()

ans = outer()
print(ans)


# output:- Hello I'm inner function
