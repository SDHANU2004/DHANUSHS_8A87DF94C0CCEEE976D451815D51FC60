def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return (n * factorial(n - 1))


number = int(5)
res = factorial(number)
print("The factorial of the given number:", res)
