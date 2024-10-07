#################### Пример_1 #######################################

def nukk_decorator(func):
    return func

def greet():
    return 'Hello World'
greet = nukk_decorator(greet)
print(greet())
print("#################################################################")
#################### Пример_2 #######################################
def null_decorator(func):
    return func

@null_decorator
def greet():
    return 'Hello World'
print(greet())
print("#################################################################")
#################### Пример_3 #######################################

# def upper(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper
#
# @upper
# def greet():
#     return 'Hello World'
#
# print(greet())

print("#################################################################")
#################### Пример_3 #######################################

import time
import sys

def time_decorator(func):
    def wrapper(*arg, **kwargs):
        start = time.time()
        result = func(*arg, **kwargs)
        end = time.time()
        elapsed = round(end - start, 2)
        print(f"Функция работала {elapsed} сукунд(ы)")
        return result
    return wrapper
@time_decorator
def digits(*args):
    total =1
    for number in args:
        total *= number ** 1000
    return len(str(total))
sys.set_int_max_str_digits(100000)

result = digits(1,2,3,4,5,6,7,8,9)
print(result)








