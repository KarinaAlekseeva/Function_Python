def sum_digits(number):
    k = 0
    while number>0:
        k += number % 10
        number//=10
    return k
    
number = int(input("Введите положительное число: "))
if number>=0:
    print("Сумма цифр: ", sum_digits(number))
else:
    print("Число меньше нуля, введите положительное число")