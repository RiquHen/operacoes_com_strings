"""Conta espaços e vogais.Dado uma string com uma frase informada
pelo usuário (incluindo espaços em branco), conte:
◦ quantos espaços em branco existem na frase.
◦ quantas vezes aparecem as vogais a, e, i, o, u."""

frase = str(input("Digite uma frase: "))
espaco = frase.count(" ") # contagem de espaços
vogais = consoantes = 0 # iniciando variaveis p/ contar vogais e consoantes
frase = ''.join(frase.split()) # removendo os espaços da frase digitada
for i in frase:
    # verifica condição para vogais
    if i in "aeiouAEIOUáÁéÈíÍóÓúÚãÃõÕêÊôÔ":
        vogais += 1
    else: # senão vogal é uma consoante
        consoantes +=1
print(f'{"="*50}\nFrase digitada: {frase}')
print(f'Na frase digitada há: {espaco} espaços.')
print(f'Na frase digitada há: {vogais} vogais.')
print(f'Na frase digitada há: {consoantes} consoantes.')
