def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result += i
        except TypeError as exc:
            incorrect_data += 1
            print(f'Некорекктный тип данных для подсчёта суммы - {i})')
    return result, incorrect_data


def calculate_average(numbers):
    try:
       # result_1 = personal_sum(numbers)
        return personal_sum(numbers)[0] / (len(numbers) - personal_sum(numbers)[1])
    except ZeroDivisionError:
        return 0
    except TypeError:
        return print(f'В numbers записан некорректный тип данных')


print(f'Результат 1: {calculate_average([5, 8, 9, 6])}')
print(f'Результат 2: {calculate_average(["Понимаю с трудом", 12, "Но вроде бы понимаю", 5])}')
print(f'Результат 3: {calculate_average(5)}')
print(f'Результат 4: {calculate_average('2, 8, 3, 1')}')