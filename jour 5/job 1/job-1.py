def Factoriel(n:int):
    if n >= 2:
        return n * Factoriel(n - 1)
    
    return n

print(Factoriel(6))