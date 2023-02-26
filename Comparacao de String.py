"""
imprime as strings  informadas pelo usuario e seus respectivos tamanhos, e as compara, se possuem o mesmo tamanho e se são iguais
"""

str1 = input('Insira primeira string para comparação: ')
str2 = input('Insira segunda string para comparação: ')

#verificando o tamanho da strings digitadas
print(f"{str1}: {len(str1)} caracteres.")
print(f"{str2}: {len(str2)} caracteres.")
print('-'*50)
if len(str1) == len(str2):
    print("As duas strings possuem o mesmo tamanho.")
else:
    print("As duas strings são de tamanhos diferentes.")
print('-'*50)
# verificando se são iguais, mesmo digitadas com letras maiuculas
if str1.lower() == str2.lower():
# lower() todas letras minusculas para comparação das strings digitadas
    print("As duas strings são iguais!")
else:
    print("As duas strings possuem conteúdo diferentes.")
print()