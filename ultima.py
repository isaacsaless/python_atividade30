# Exercício Python 30: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

nomes = []
idades = []
sexos = []
MediaIdade = 0
MaiorIdadeH = 0
NomeMaisVelho = ""

for i in range(0,4):
    nome = str(input('Digite seu nome: '))
    nomes.append(nome)
    idade = int(input('Digite sua idade: '))
    idades.append(idade)
    sexo = int(input(""""Digite '1' se for homem, ou '2' se for mulher: """ ))
    if sexo > 2 or sexo < 0:
        print('Digite um número válido')
        break
    if sexo == 1 and max(idades):
        NomeMaisVelho = nome
MediaIdade = (sum(idades)/4)
print(f'A média da idade do grupo é de {MediaIdade}')
print(NomeMaisVelho)