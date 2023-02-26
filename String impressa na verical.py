# Faça um programa que solicite o nome do usuário e imprima-o na vertical.

# usuário informa o nome
nome = str(input("Digite seu nome: "))
# declaração variávels que vai armazenar os caracteres do nome informado
c = ''
# percorre todo o nome
for i in nome:
    c += i # concatena o caracter do nome
    print(f"{i:^5}{c:<20}")  # imprime [i]-caracter do nome percorrido
#[c]-string armazenada em c

print(15*"=")
# percorre o nome de trás pra frente
for i in nome[len(nome)::-1]:
    print(nome)
    nome = nome.rstrip(i) # retira um caracter do nome a cada vez que roda o loop for