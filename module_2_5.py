def get_matrix(n, m, value):
    matrix = []             # создаем пустой список
    for i in range(n):     # перебираем ряды 'n' повторов
        pol = []         # полоса (или ряд)
        for j in range(m):  # перебираем столбцы 'm' повторов
            pol.append(value)  # добавляем значение элемента
            matrix.append(pol)
        return matrix    # возвращаем значение переменной  matrix


tabl = get_matrix(3, 3, 6)
print(tabl)
tabl_1 = get_matrix(4,3, 1)
print(tabl_1)
tabl_2 = get_matrix(2, 2, 11)
print(tabl_2)
