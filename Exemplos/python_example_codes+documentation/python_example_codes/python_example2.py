#Mesmas funções do código anterior, sendo que foi adicionado "_2" no final de seus nomes.


import time
import random

var_state=False

def F1_2():
    #Função que avisa que o status da operação é verdadeiro e gera um valor aleatório para contador.
    var_state=True
    F2_2(random.randrange(1,10))
    

def F2_2(randon_counter):
    #Função que primeiramente verifica se o contador já está em seu valor máximo (10).
    #Caso não esetja, ela o incrementa (desde que o status seja verdadeiro).
    #Além disso, gera o delay de 2 s e acionar a função F3 
    var_counter=randon_counter
    if var_counter==10:
        F4_2()
    else:
        if var_state==True:        
            var_counter=counter+1        
        time.sleep(2)
        F3_2()

def F3_2():
    #Função que identifica se o contador deve ser resetado (caso seja igual a 10) e aciona a função F4.
    if var_counter==10:
        var_reset=True
    F4_2()

def F4_2():
    #Função que reseta o contador caso isso seja demandado pela variável reset.
    if var_reset==True:
        counter=0
    var_reset=False
    
var_counter=0

while True:
    var_state=False
    print("Novo ciclo")    
    F1_2()
    time.sleep(5)
    



