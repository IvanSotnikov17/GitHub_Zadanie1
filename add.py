def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ValueError("Ошибка: деление на ноль!")
    return a / b

def calculate(a, op, b):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return sub(a, b)
    elif op == '*':
        return mul(a, b)
    elif op == '/':
        return div(a, b)
    else:
        raise ValueError("Неизвестная операция")
    
    def parse():
    a = float(input("Введите первое число: "))
    op = input("Введите операцию (+, -, *, /): ")
    b = float(input("Введите второе число: "))
    return a, op, b