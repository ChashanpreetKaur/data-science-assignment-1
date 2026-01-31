threshold = 100
product = 1
currentNumber = 1

while product <= threshold:
  product *= currentNumber
  if product > threshold:
    break
  currentNumber += 1
 print("Final product:", product)
 print("Number causing exceed:", currentNumber)
  


