#!/usr/local/bin/python
# coding : utf-8

#por padrao o input recebe string
# A = input()
# B = input()


#Recebe duas variaveis na mesma linha 5 6 
A = input()
 
#converter para o tipo int
A = float(A)
 

if A >=7:
    print("Aluno aprovado")
elif A >= 5:
    print("Recuperação")
else:
    print("Reprovado")