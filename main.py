from fake_math import divide as fake_div
from true_math import divide as true_div

result1 = fake_div(75, 5)
result2 = fake_div(25, 0)
print(result1)
print(result2)
result3 = true_div(15, 3)
result4 = true_div(25, 0)
print(result3)
print(result4)