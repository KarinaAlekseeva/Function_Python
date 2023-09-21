import math

print("Добро пожаловать в калькулятор. Выберите операцию из списка: ")

print("|a| Сложить")

print("|b| Вычесть")

print("|c| Умножить")

print("|d| Разделить")

print("|e| Возвести в степень")

print("|f| Извлечь квадратный корень")

print("|g| Вычислить факториал")

print("|h| Вычислить синус")

print("|i| Вычислить косинус")

print("|j| Вычислить тангенс")

print("|k| Выход")

oper = input()

def add(a,b):
    result = a + b
    return result

def diff(a,b):
    result = a - b
    return result

def mult(a,b):
    result = a * b
    return result

def mod(a,b):
    result = a / b
    return result

def step(a,b):
    result = a ** b
    return result

def sqrt(a):
    result = math.sqrt(a)
    return result

def fact(a):
    if a > 0:
        for i in range(1, a): a = a * i  
    elif a == 0: 
        a = 1  
    return a

def sin(a):
    result = math.sin(a)
    return result

def cos(a):
    result = math.cos(a)
    return result

def tan(a):
    result = math.tan(a)
    return result

while oper!= "k":
    match oper:
        case "a":
            try:
                operand1 = float(input("Введите первое число: "))

                operand2 = float(input("Введите второе число: "))

                print("Результат: ", add(operand1,operand2))

                oper = input("Введите операцию: ")
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ")

        case "b":
            try:
                operand1 = float(input("Введите первое число: "))

                operand2 = float(input("Введите второе число: "))

                print("Результат: ", diff(operand1,operand2))

                oper = input("Введите операцию: ")
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ")

        case "c":
            try:
                operand1 = float(input("Введите первое число: "))

                operand2 = float(input("Введите второе число: "))

                print("Результат: ", mult(operand1,operand2))

                oper = input("Введите операцию: ")
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ")
        
        case "d":
            try:
                operand1 = float(input("Введите первое число: "))

                operand2 = float(input("Введите второе число: "))

                if operand2 != 0:
                    print("Результат: ", mod(operand1,operand2))

                    oper = input("Введите операцию: ")
                else:
                    print("На ноль делить нельзя!")

                    oper = input("Введите операцию: ") 
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ")

        case "e":
            try:
                operand1 = float(input("Введите первое число: "))

                operand2 = float(input("Введите степень, в которую хотите возвести число: "))

                print("Результат: ", step(operand1,operand2))

                oper = input("Введите операцию: ")
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ")

        case "f":
            try:
                operand1 = float(input("Введите первое число: "))
            
                if operand1 >=0:

                    print("Результат: ", sqrt(operand1))

                    oper = input("Введите операцию: ") 
                else:
                    print("Не существует корня отрицательного числа")

                    oper = input("Введите операцию: ")
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ")

        case "g":
            try:
                factorial = int(input("Введите число: "))  
                if factorial >=0:
                    print("Результат: ", fact(factorial))

                    oper = input("Введите операцию: ") 
                else:  
                    print("Не существует факториала отрицательного числа!") 

                    oper = input("Введите операцию: ") 
            except(ValueError): 
                print("Введите корректное число")

                oper = input("Введите операцию: ") 
                
        case "h":
            try:
              operand1 = float(input("Введите число: "))

              print("Результат: ", sin(operand1))  

              oper = input("Введите операцию: ")
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ") 

        case "i":
            try:
              operand1 = float(input("Введите число: "))

              print("Результат: ", cos(operand1))  

              oper = input("Введите операцию: ")
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ") 

        case "j":
            try:
              operand1 = float(input("Введите число: "))

              print("Результат: ", tan(operand1))  

              oper = input("Введите операцию: ")
            except(ValueError):
                print("Введите корректное число")

                oper = input("Введите операцию: ") 
                             
        case _:
            print("Данной операции нет в списке")

            oper = input("Введите операцию: ")
            
        