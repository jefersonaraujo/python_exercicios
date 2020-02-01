#!/usr/local/bin/python
# coding : utf-8


#Recebe duas variaveis na mesma linha 5 6 
A,B = input().split()
 
#converter para o tipo int
A = float(A)
B = float(B)

#Processamento

media = (A + B)/2
resposta =''

if media >= 7:
    resposta  ='Aprovado'
elif  media >=4:
    resposta  ='Recuperacao'
else:
    resposta  ='Reprovado'

    
    
print(resposta)