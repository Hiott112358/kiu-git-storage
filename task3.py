#Не уверен, что я сделал все правильно и нужно было делать так 
def validator(fn):
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        print('result = ', result)
        return result
    return inner
@validator
def greater_than(num):
    if num > 0:
        return num , 'Больше введенного'
    else: 
        return 'error'    
greater_than(123)

@validator
def less_than(num):
    if num < 100:
        return num, 'error'
    else:
        return num  
less_than(101)

@validator
def starts_with(strok):
    rand_strok = input()
    if strok in rand_strok:
        return strok
    else:
        return 'error'
starts_with('str')

@validator
def some_in(block):
    users_block = input()
    if block in users_block:
        return block
    else:
        return 'error'
some_in('1,2,3')

