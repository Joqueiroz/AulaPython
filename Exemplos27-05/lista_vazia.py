<<<<<<< HEAD
import time

my_list = [] #criando uma lista vazia

for i in range(5):
    my_list.append(i + 1)

print(my_list)    

#lista vazia 2
my_list2 = [] #segunda lista vazia

for i in range(5):
    my_list2.insert(0, i + 1)

print(my_list2)   

#terceira lista
my_list3 = [10, 1, 8, 3, 5]

total = 0

for i in range(len(my_list3)):
    total = total + my_list3[i]

print(total)

total = 0
for i in my_list3:
    total += i  

print(total)      

#reodenando a lista
# my_list3[0], my_list3[4] = my_list3[4], my_list3[0]
# my_list3[1], my_list3[3] = my_list3[3], my_list3[1]

# print(my_list3)

#Reordenando sem saber tamanho da lista
tamanholista = len(my_list3)
for i in range(tamanholista // 2):
    my_list3[i], my_list3[tamanholista - i - 1] = my_list3 [tamanholista - i - 1],my_list3[i]

print(my_list3)    

=======
import time

my_list = [] #criando uma lista vazia

for i in range(5):
    my_list.append(i + 1)

print(my_list)    

#lista vazia 2
my_list2 = [] #segunda lista vazia

for i in range(5):
    my_list2.insert(0, i + 1)

print(my_list2)   

#terceira lista
my_list3 = [10, 1, 8, 3, 5]

total = 0

for i in range(len(my_list3)):
    total = total + my_list3[i]

print(total)

total = 0
for i in my_list3:
    total += i  

print(total)      

#reodenando a lista
# my_list3[0], my_list3[4] = my_list3[4], my_list3[0]
# my_list3[1], my_list3[3] = my_list3[3], my_list3[1]

# print(my_list3)

#Reordenando sem saber tamanho da lista
tamanholista = len(my_list3)
for i in range(tamanholista // 2):
    my_list3[i], my_list3[tamanholista - i - 1] = my_list3 [tamanholista - i - 1],my_list3[i]

print(my_list3)    

>>>>>>> c152a31d2f3c0e1889a187649be69fae7d8ffd96
time.sleep(3)