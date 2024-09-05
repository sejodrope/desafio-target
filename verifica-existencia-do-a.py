def count_a(string):
    count = string.lower().count('a')
    return count

texto = input("Digite uma string: ")
ocorrencias = count_a(texto)

if ocorrencias > 0:
    print(f"A letra 'a' aparece {ocorrencias} vez(es) na string.")
else:
    print("A letra 'a' não aparece na string.")