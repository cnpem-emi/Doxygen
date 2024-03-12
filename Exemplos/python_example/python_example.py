import time
import random

var_state=False
var_reset=False

def F1():    
    #Função que avisa que o status da operação é verdadeiro e gera um valor aleatório para contador.
    global var_state
    var_state=True
    F2(random.randrange(1,11)) #Números aleatórios de 1 a 10.
    

def F2(randon_counter):
    #Função que primeiramente atualiza o contador para um valor aleatório (caso seja maiorq ue o atual).
    #Depois, verifica se o contador já está em seu valor máximo (10).
    #Caso não esetja, ela o incrementa (desde que o status seja verdadeiro).
    #Além disso, gera o delay de 2 s e acionar a função F3. 
    global var_counter
    global var_reset
    global var_state
    print("Variável Aleatória:", randon_counter)
    if randon_counter>var_counter:
        var_counter=randon_counter
    print("Variável Counter:", var_counter)
    if var_counter==10:
        var_reset=True
        F4()
    else:
        time.sleep(2)
        if var_state==True:        
            var_counter=var_counter+1
            print("Variável Counter (pós acréssimo):", var_counter)
        F3()

def F3():
    global var_counter
    global var_reset
    #Função que identifica se o contador deve ser resetado (caso seja igual a 10) e aciona a função F4.
    if var_counter==10:
        var_reset=True
    else:
        var_reset=False
    print("Variável Reset:", var_reset)
    F4()

def F4():
    global var_reset
    global var_counter
    #Função que reseta o contador caso isso seja demandado pela variável reset.
    if var_reset==True:
        var_counter=0
    var_reset=False
    
var_counter=0

while True:    
    print("Novo ciclo")    
    F1()
    time.sleep(5)
    



