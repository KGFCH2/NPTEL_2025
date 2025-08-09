pin = int(input())
square = pin ** 2
digit_sum = sum(int(digit) for digit in str(square))
if digit_sum == pin:
  print("Neon Number")
else:
    print("Not Neon Number")