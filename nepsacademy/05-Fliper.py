#!/usr/local/bin/python
# coding : utf-8

#por padrao o input recebe string
# A = input()
# B = input()


#Recebe duas variaveis na mesma linha 5 6 
P,R = input().split()
 
#converter para o tipo int
P = int(P)
R = int(R)

if P ==0:
    print("C")
elif R ==0:
    print("B")
else:
    print("A")