import random
def validator(fn):
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        print('result = ', result)
        return result
    return inner
@validator
def greater_than(num):
    for i in range(random.randint(0, 100)):
        print(i)
        if num > i:
            return num 
        else: 
            return 'error'
    print(i)
greater_than(1)
