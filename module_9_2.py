first_strings = ['Март', 'Май', 'Июнь', 'Август', 'Январь', 'Декабрь']
second_strings = ['Октябрь', 'Ноябрь', 'Апрель', 'Февраль', 'Июль', 'Сентябрь']
combined_strings = first_strings + second_strings

first_result = [len(x) for x in first_strings if len(x) >= 5]

second_result = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]

third_result = {x: len(x) for x in combined_strings if len(x) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
