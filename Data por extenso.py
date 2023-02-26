"""Programa que solicite a data de nascimento
(dd/mm/aaaa) do usuário e imprime a data com o nome do mês por extenso.
◦ Data de Nascimento: 29/10/1984
Você nasceu em  29 de Outubro de 1984."""
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto",
         "setembro", "outubro", "novembro", "dezembro"]

#recebe a data do nascimento
nascimento = str(input("Data de nascimento(separando dia, mes e ano): "))

# tratando o separador do dia, mes e ano
dat = ''
for d in nascimento:
    if d.isnumeric(): #verifica se é número
        dat += d # add número na variável dat
    else: # se não for número, é acrescentado / na variável dat
        dat += '/'
# transforma a variável dat em um lista[dia, mes, ano]
data = dat.split("/")

print(f"{40*'='}\nData de Nascimento: {nascimento}")

# separa o mes, pelo indice da lista data
mes = int(data[1])
# de acordo com os itens da lista data informa seus valores para compor a data,
# PS: o valor inteiro do mes é retirado de acordo com o indice na lista meses
print(f"Você nasceu em: {data[0]} de {meses[mes-1]} de {data[2]} ")
print('='*50)