#scrie codul mai jos:
for numar in range(1, 101):
  if numar % 3 == 0:
    print("Fizz")
  elif numar % 5 == 0:
    print("Buzz")
  elif numar % 3 == 0 and numar % 5 == 0:
    print("FizzBuzz")
  else:
    print(numar)
  