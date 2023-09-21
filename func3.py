def is_even(number):
    if number % 2 == 0:
        result = True
    else:
        result = False
    return result
number = int(input("Введите число: "))
print(is_even(number))