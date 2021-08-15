# TSP fuerza bruta 
from sys import maxsize
import timeit 
# Numero de nodos
V = 4

# implementacion del TSP 
def travellingSalesmanProblem(graph, s): 

    # vertices excepto el inicial 
    vertex = [] 
    for i in range(V): 
        if i != s: 
            vertex.append(i) 

    # minimo ciclo hamiltoniano 
    min_path = maxsize 
    min_route=[]

    while True: 

        # guardar peso o costo de la ruta 
        current_pathweight = 0

        # calcular peso de la ruta actual 
        k = s 
        for i in range(len(vertex)): 
            current_pathweight += graph[k][vertex[i]] 
            k = vertex[i] 
        current_pathweight += graph[k][s] 

        # update minimo
        if (current_pathweight<min_path):
            min_path = current_pathweight
            min_route= vertex[:]
        
        if not next_permutation(vertex): 
            break

    return (min_path, [0]+min_route) 

# funcion para conseguir la siguiente permutacion 
def next_permutation(L): 

    n = len(L) 

    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]: 
        i -= 1

    if i == -1: 
        return False

    j = i + 1
    while j < n and L[j] > L[i]: 
        j += 1
    j -= 1

    L[i], L[j] = L[j], L[i] 

    left = i + 1
    right = n - 1

    while left < right: 
        L[left], L[right] = L[right], L[left] 
        left += 1
        right -= 1

    return True


if __name__ == "__main__": 
    
    graph = [[0, 10, 15, 20], 
             [10, 0, 35, 25], 
             [15, 35, 0, 30], 
             [20, 25, 30, 0]] 
    s = 0
    print(travellingSalesmanProblem(graph, s)) 

    SETUP_CODE = ''' 
from __main__ import travellingSalesmanProblem '''
  
    TEST_CODE = ''' 
graph = [[0, 10, 15, 20], 
             [10, 0, 35, 25], 
             [15, 35, 0, 30], 
             [20, 25, 30, 0]]
s=0
travellingSalesmanProblem(graph, s) '''
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 1000) 
   
    print('Tiempo ejecucion: {}'.format(min(times)/1000.0))
    