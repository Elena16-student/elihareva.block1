
calls = 0 #создаем переменную, это начало отсчета, если поставим напр. calls = 2,то вызовов будет на консоли 7 в данном случае
def count_calls():
    global calls #после global должно стоять название переменной, иначе выдает ошибку
    calls += 1 #(+=, -=, *= и /=) называются дополненными арифметическими заданиями, в циклах += эквивалентно calls = calls+1


def string_info(string_):
    count_calls()
    string = () #назначаем аргумент
    string += len(string_), string_.upper(), string_.lower()
    return string #возвращаем кортеж из длины строки и слова в верх. и нижнем регистре


def is_contains(string_, list_to_search):
    count_calls()
    bool = True #далее приводим шрифт к общему знаменателю, # у нас к заглавному ( можно наоборот к lower)
    bool_ = ' '.join(list_to_search).upper() #см. тему "строки" и ссылку на 41  вопрос по строкам
    if bool_.find(string_.upper()) == -1: # find выдает -1 , если искомая строка в подстроке не найдена
        bool = False # если строки нет в подстроке, то выдается ложь соответственно
    return bool


print(string_info('Visantia'))
print(string_info('Stambul'))
print(string_info('Rom'))
print(is_contains('Стол', ['столовая', 'подстолье', 'застолье']))
print(is_contains('notebook', ['ball', 'note', 'rice']))

print(calls)