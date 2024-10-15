def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        #if result > 1: #Начинаем перебор с 2, т.к. единица вне конкуренции (не проста,  но и не составная)
        if all((result % i != 0) for i in range(2, int(result))):
            return "Простое" #простое число делится на 1 и на самое себя
        else:
            return 'Cоставное'
    return wrapper


@is_prime
def sum_three(a, b, c):
    result = a + b + c
    print(result)
    return result


test_1 = sum_three(3, 7, 3)
print(test_1)
test_2 = sum_three(654, 9, 2)
print(test_2)
