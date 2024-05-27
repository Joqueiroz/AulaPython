<<<<<<< HEAD
import time

#Número maior inicial
M = -9999999999


#Pede um número pro usuário
N = int(input('Digite um número inteiro ou "-1" para sair: '))

#Enquanto o número for diferente de -1, repete
while N != -1:
    #O número é maior que o maior número atual?
    if N > M:
        #Caso verdadeiro, maior número recebe numero.
        M = N
    #Solicita o próximo número
    N = int(input('Digite um número inteiro ou "-1" para sair: '))

#Fala o maior número gravado
=======
import time

#Número maior inicial
M = -9999999999


#Pede um número pro usuário
N = int(input('Digite um número inteiro ou "-1" para sair: '))

#Enquanto o número for diferente de -1, repete
while N != -1:
    #O número é maior que o maior número atual?
    if N > M:
        #Caso verdadeiro, maior número recebe numero.
        M = N
    #Solicita o próximo número
    N = int(input('Digite um número inteiro ou "-1" para sair: '))

#Fala o maior número gravado
>>>>>>> c152a31d2f3c0e1889a187649be69fae7d8ffd96
print("O maior número digitado foi", M)