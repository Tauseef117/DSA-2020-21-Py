numbers = [110,120,50,160,170,105]
large=numbers[0]
for i in numbers:
  if i>large:
      large=i
print(f"largest is {large}")

numbers.sort()
print(f"largest is {numbers[-1]}")
print("largest is",numbers[0])
