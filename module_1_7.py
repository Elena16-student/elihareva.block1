grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
Student = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
Student_alph = sorted(Student)
#print(Student_alph)
A = [5, 3, 3, 5, 4]
middle = sum(A)/len(A)
#print(middle)
middle_mark_A = sum(grades[0])/len(grades[0])
middle_mark_B = sum(grades[1])/len(grades[1])
middle_mark_J = sum(grades[2])/len(grades[2])
middle_mark_K = sum(grades[3])/len(grades[3])
middle_mark_S = sum(grades[4])/len(grades[4])
middle_mark_1 = ((sum(grades[0])/len(grades[0])), (sum(grades[1])/len(grades[1])),
                 (sum(grades[2])/len(grades[2])), (sum(grades[3])/len(grades[3])), (sum(grades[4])/len(grades[4])))
mark = ((Student_alph[0], middle_mark_A), (Student_alph[1], middle_mark_B), (Student_alph[2],
middle_mark_J), (Student_alph[3], middle_mark_K), (Student_alph[4], middle_mark_S))
dict1 = dict(mark)
print(dict1)
#Dict2 = dict(zip(Student_alph, middle_mark_1)) # , более простое решение
#print(Dict2)

