'''Faça um programa que peça para 5 pessoas a sua idade, ao final o
programa deverá verificar se a média das idades informadas varia entre
0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta
ou idosa, conforme a média calculada'''
soma = 0

for i in range (5):
     
    idade = int(input('Informe a idade: '))
    soma += idade
media = soma/5 
if idade <= 25:
    print('jovens')
elif media <60:
    print('Adultos')
else:
    print('idosa')