
my_list = [1, 4, 2, 9, 7, 2, 1, 8, 3, 3, 2, 19]             # Create example list

print("Max : %d" %max(my_list))                             # Get max of list
print("Min : %d" %min(my_list))                             # Get min of list


a=0

for i in range(len(my_list)):
   if my_list[i] >= a: a=my_list[i]

print("Valor Maximo : %d " %a)

a=99

for i in range(len(my_list)):
   if my_list[i] <= a: a=my_list[i]

print("Valor Minimo: %d " %a)