


import numpy as np

#valor= np.array([2,6,8,7,3,4,6,5,10,9,8,11,12,15,6,8,13,14,15,16,13,14,15,26,13,9,25,26])
#peso = np.array([7,3,3,5,4,7,5,4,15,10,17,3,6,11,6,14,4,8,9,10,14,17,9,24,11,17,12,14])
#W_capacidad = 50


valor = np.array([60, 100, 120, 70, 45, 90, 200, 80, 30, 40])
peso = np.array([10,  20,  30, 15,  5, 25,  55, 15, 10 ,5])
                 
W_capacidad = 60




def geedy_mochila(val, pes,capacidad,Knapsack_bag):

    def ratio(val,pes):   
        #2. Use of a score or efficiency function, i.e. the profit to weight ratiodef ratio(valor,peso)
        score = []
        for i in range(len(val)):
                #appending the score of each iteration of the value and weight arrays
            # m=(valor[i]/peso[i])
            score = np.append(score,(val[i]/pes[i]))   
        #print(score)
        return score
        
    scores_ratio = ratio(val,pes)
    indicies = np.argsort(-scores_ratio)
    Knapsack_index = np.zeros(len(val))
    Knapsack_bag
    
    
    
    for i in range(len(val)):
        items = indicies[i]
        if((Knapsack_bag+peso[items]) <= capacidad):
            Knapsack_index[items] = 1
            Knapsack_bag += pes[items]


    Total_pesos = np.sum(pes[Knapsack_index==True])        
    Invididual_pesos =  pes[Knapsack_index==True]
    Total_valor = np.sum(val[Knapsack_index==True])
    Individual_valor =  val[Knapsack_index==True]
    #Indices_profit = items[Knapsack_index==True]
    return(Total_pesos,Invididual_pesos,Total_valor,Individual_valor)



a,b,MAX_greedy,d = geedy_mochila(valor,peso,W_capacidad,Knapsack_bag = 0)


print("Peso Total de la Mochila, ",a,' Pesos individuales:',b)
print("Valor total de mochila es, ",MAX_greedy,' valores individuales:',d)

#print("SCORE",scores_ratio)
##print(Knapsack_index)
#print("PESO TOTAL",Total_weight)
#print("Invididual_weight",Invididual_weight)


