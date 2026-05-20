# -*- coding: utf-8 -*-

#RESPOSTAS DA ATIVIDADE 2:

#PERGUNTA 1:

numero1 = float(input("Digite o 1° número: "))
numero2 = float(input("Digite o 2° número: "))
soma = numero1 + numero2
print(soma)

#PERGUNTA 2:
numero = int(input("Digite o 1° número: "))
if(numero % 2 == 0):
    print("Número par")
else:
    print("Número ímpar")

#PERGUNTA 3:
numero1 = float(input("Digite o 1° nota: "))
numero2 = float(input("Digite o 2° nota: "))
numero3 = float(input("Digite o 3° nota: "))
media = (numero1 + numero2 + numero3)/3
print("A média é:", media)

"""#PERGUNTA 4:
a) O que o código acima faz?

Resposta:
Exibe os 10 primeiros números da Sequência de Fibonacci

b) O que significam as variáveis a e b no início do código?

Resposta:
Variáveis de inicialização, a recebe 0 e b recebe 1.

c) Como você modificaria o código para gerar os primeiros 20 números da
sequência de Fibonacci?

Resposta:
Modificaria a parte do range, ao invés de rodar 10 vezes ele roda 20, ficaria assim: for _ in range(20)

d) Como você modificaria o código para começar a sequência de Fibonacci
com outros dois números, por exemplo, 2 e 3?

Resposta:
Só mudar os valores das variáveis de inicialização, a recebe 2 e b recebe 3.

e) Qual é a função do loop for neste código?

Resposta:
Rodar o mesmo código várias vezes, ele executa o código que está dentro dele
quantas vezes forem definadas.

"""

#PERGUNTA 5

numero = float(input("Digite o 1° número: "))
if(numero >= 9):
    print("Desempenho excelente!")
elif(numero >= 7):
    print("Desempenho bom!")
elif(numero >= 5):
    print("Desempenho razoável!")
else:
    print("Desempenho insuficiente!")

#PERGUNTA 6:
numero = float(input("Digite o 1° número: "))
if(numero == 0):
    print("zero")
elif(numero > 0):
    print("positivo")
else:
    print("negativo")

#PERGUNTA 7:
numero = float(input("Digite um número: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i:2} = {resultado}")
