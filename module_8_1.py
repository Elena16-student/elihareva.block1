
# except TypeError:
#     if type(a) == str and type(b) == int or float:
#       print(f'(str(a+b))')

def add_everything_up(a, b):
    try:
        return (a + b)
    except TypeError:
        return str(a) + str(b)

print(add_everything_up(6 , 'окно'))
print(add_everything_up(8.5, "стол"))
print(add_everything_up('дверь', 701.22))
print(add_everything_up(122, 701.22))