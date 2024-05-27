import time
numero = float(input("Digite um numero inteiro positivo:", ))
while(numero < 0):
    numero = float(input("ERROR!\nDigite um numero inteiro positivo:", ))
resultado = numero % 2
if resultado == 0:
   print('""P-A-R!!!""')
if resultado == 1:
   print('"Tente outra vez"')
   time.sleep(5)