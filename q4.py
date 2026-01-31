from random import random
values = [random() for i in range(20)]
x = random()
values.sort()
indices = [i for i, v in enumerate(values) if v>= x]
print("Sorted values:", values)
print("x:", x)
if indices:
  print("First matching index:", indices[0])
else:
  print("No value >= x")
