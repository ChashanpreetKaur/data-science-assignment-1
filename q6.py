def distribution(numbers):
  total = len(numbers)
  result = {}

  for value in sorted(set(numbers)):
    count = sum(1 for n in numbers if n <= value)
    result[value] = (count / total) * 100

  return result

print(distribution([3, 1, 2, 3, 4, 2]))
