def verifica_fibonacci(numero):
    fibonacci= [0, 1]

    while fibonacci[-1] < numero:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

        if numero in fibonacci:
            return f"O número {numero} pertence à sequencia de Fibonacci"
        else:
            return f"O número {numero} não pertence à sequencia de Fibonacci"


numero = int(input("digite um numero:"))
print(verifica_fibonacci(numero))