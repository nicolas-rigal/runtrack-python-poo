# caré parfait 1-1-3-5-
def fibonacci(n):
    if n < 0:
        return "la suite de fibinacci ne peut pas être negatif "
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
  
print(fibonacci(-1))    
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))
print(fibonacci(9))
print(fibonacci(10))
print(fibonacci(11))
print(fibonacci(12))
print(fibonacci(13))
print(fibonacci(14))
print(fibonacci(15))