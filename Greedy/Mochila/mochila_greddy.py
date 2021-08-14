


import numpy as np

valor= np.array([60,10,10,24,50])
peso = np.array([10,2,5,8,4])

#valor= np.array([10,24,60,10,50])
#peso = np.array([5,8,10,2,4])

W_capacity = 10

def ratio(val,pes):   
    #2. Use of a score or efficiency function, i.e. the profit to weight ratiodef ratio(valor,peso)
    score = []
    for i in range(len(val)):
            #appending the score of each iteration of the value and weight arrays
        # m=(valor[i]/peso[i])
        score = np.append(score,(val[i]/pes[i]))   
    print(score)
    return score
    
scores_ratio = ratio(valor,peso)
indicies = np.argsort(-scores_ratio)
Knapsack_index = np.zeros(len(valor))
Knapsack_bag=0



for i in range(len(valor)):
    items = indicies[i]
    if((Knapsack_bag+peso[items]) <= W_capacity):
        Knapsack_index[items] = 1
        Knapsack_bag += peso[items]
        
Total_weight = np.sum(peso[Knapsack_index==True])        
Invididual_weight =  peso[Knapsack_index==True]
Total_profit = np.sum(valor[Knapsack_index==True])
Individual_profit =  valor[Knapsack_index==True]
#return(Total_weight,Invididual_weight,Total_profit,Individual_profit)




print("SCORE",scores_ratio)
print("indices",indicies)
print(Knapsack_index)
print("PESO TOTAL",Total_weight)
print("Invididual_weight",Invididual_weight)


