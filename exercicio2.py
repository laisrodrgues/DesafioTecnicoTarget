def verifica_letra_a(string):
    quantidade_a = string.lower().count('a')
    if quantidade_a > 0:
        return f"A letra 'a' aparece {quantidade_a} vezes na string"
    else:
        return f"A letra 'a' não aparece na string"

string = input("Digite uma string: ")
print(verifica_letra_a(string))
