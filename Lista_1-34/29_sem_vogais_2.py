<<<<<<< HEAD
import time

s_vog = ""
uw = input("Declare uma palavra: ").upper()

for letra in uw:
    if letra in "AEIOU":
        continue
    else:
        s_vog += letra
    time.sleep(1)

print("Palavra sem vogais:", s_vog)

=======
import time

s_vog = ""
uw = input("Declare uma palavra: ").upper()

for letra in uw:
    if letra in "AEIOU":
        continue
    else:
        s_vog += letra
    time.sleep(1)

print("Palavra sem vogais:", s_vog)

>>>>>>> c152a31d2f3c0e1889a187649be69fae7d8ffd96
time.sleep(2)