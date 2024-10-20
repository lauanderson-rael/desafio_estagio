def pertence_fibonacci(num):
    a, b = 0, 1
    fibonacci_sequence = [a, b]

    while b <= num:
        a, b = b, a + b
        fibonacci_sequence.append(b)

    return num in fibonacci_sequence

numero = int(input("Informe um número: "))
if pertence_fibonacci(numero):
    print(f"{numero} pertence à sequência de Fibonacci.")
else:
    print(f"{numero} não pertence à sequência de Fibonacci.")
