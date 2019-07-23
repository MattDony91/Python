# calc.py

def my_plus(a, b):
    return a + b

def my_sub(a, b):
    return a - b

def my_mul(a, b):
    return a * b

def my_div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.'