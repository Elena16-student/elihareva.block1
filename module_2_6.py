
def parole(n):
     result = ''
     for i in range(1, n):
         for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result += str(i) + str(j)
     return result


print(parole(int(input('Роковое число: '))))
print(parole)


#print('Роковое число: ')
#print(parole(int(input())))


#for n in range(3, 21):
# result = str()
# for i in range(1, 21):
#      for j in range(i+1, 21):
#         if n % (i + j) == 0:
#            result += f"{i}{j}"
# print (f'{n} - {result}')

