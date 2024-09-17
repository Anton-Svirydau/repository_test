# decorators

""""""


# def my_decorators(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#
#     return wrapper
#
#
# # def say_hello():
# #     print("Hello")
# #
# #
# # my_decorators(say_hello)()
#
# @my_decorators
# def say_hello():
#     print("Hello")
#
#
# say_hello()


def my_decorators(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

    return wrapper


# @my_decorators
# def say_hello(*, name: str) -> None:
#     print(f"Hello, {name}")
#
#
# say_hello(name="Sasha")

@my_decorators
def add_numbers(*, a: int, b: int) -> int:
    print("Adding numbers...")
    return a + b


result = add_numbers(a=3, b=4)

print(result)
  