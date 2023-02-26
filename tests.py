import math

# 1 esep
def fx(x, n):
  sum = 0
  for i in range(0, n, 2):
    sum += (x**i) / math.factorial(i)
  return sum


# 13 esep

""" def fx(x, n):
  if abs(x) > 1:
    return "Ошибка: |x| должно быть меньше или равно 1"
  else:
    sum = 0
    for i in range(0, n, 2):
        znak = 1 if i%4 == 0 else -1
        sum += znak * (x**i) / (math.factorial(i) * (2**(i//2)) * (i//2 + 1))
        print(sum)
    return sum """

# 12 esep

def fx(x,n):
    if abs(x) > 1:
        return "Ошибка: |x| должно быть меньше"
    else:
        sum = 0
        for i in range(0, n, 2):
            znak = 1 if i%4 < 2 else -1
            sum += znak * (x**i) / (math.factorial(i) * (2**(i//2)) * (i//2 + 1))
            print(sum)
        return sum 

x = float(input("Введите значение x: "))
n = int(input("Введите значение n: "))
print("y = ", fx(x, n))
