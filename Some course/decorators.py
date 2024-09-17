# decorators

""""""


def my_decorators(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


# def say_hello():
#     print("Hello")
#
#
# my_decorators(say_hello)()

@my_decorators
def say_hello():
    print("Hello")


say_hello()
