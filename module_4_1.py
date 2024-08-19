from fake_math import divide as fake_0
from true_math import divide as true_1

result_1 = true_1(4, 6)
result_2 = true_1(4, 0)
result_3 = fake_0(5, 3)
result_4 = fake_0(7, 0)
print(result_1)
print(result_2)
print(result_3)
print(result_4)