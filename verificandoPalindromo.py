"""Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita
da direita para esquerda ou vice−versa. Por exemplo:OSSO e OVO são palíndromos.
Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS
é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
Programa que lê uma seqüência de caracteres e mostra se é um
palíndromo ou não."""

inv_palindromo = "" # variavel que vai armazenar de tras pra frente
palindromo = str(input("Digite uma frase ou palavra para verificar se é um palíndromo: "))  # captura do que foi digitado
for i in palindromo[::-1]: #percorrendo o digitado de tras pra frente
    inv_palindromo += i # criando de tras pra frente
print(50*"=")
# removendo todo os espaços e comparando se as string são iguais
if palindromo.replace(" ", "") == inv_palindromo.replace(" ", ""):
    print("A frase informada é um palíndromo.")
else:
    print("A frase informada não é um palíndromo.")

