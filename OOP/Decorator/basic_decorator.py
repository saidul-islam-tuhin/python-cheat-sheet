def my_function(func):
    print("Before called outer function")

    func()

    print("After call outer function")

@my_function
def outer_func():
    print("outer function work")


"""
def without_using_decorator(func):
    print("Before called outer function")

    func()

    print("After call outer function")

def outer_func():
    print("outer function work")

# If we use decorator then we haven't use this line
without_using_decorator(outer_func)

"""