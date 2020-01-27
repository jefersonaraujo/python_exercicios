#!/usr/local/bin/python
# coding : utf-8

#por padrao o input recebe string
# A = input()
# B = input()


#Recebe duas variaveis na mesma linha 5 6 
A,B = input().split()
#converter para o tipo int
A = int(A)
B = int(B)

print("O valor da soma é {} e o valor da divisão e {:.3f}".format(A + B, A/B))
