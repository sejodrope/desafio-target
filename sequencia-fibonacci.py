def fibonacci_check(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    if b == num:
        return True
    return False

numero = int(input("Digite um número para verificar: "))
if fibonacci_check(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")