from math import log2
from random import randint
from statistics import mean
from time import time

def merge(A, L, R) -> None:
    """
    Implementer Mergesort i Java eller Python ud fra bogens pseudokode
    (side 31 og 34). Lad input være et array (Java) eller liste (Python) 
    af heltal. Som værdien 1 (pseudokode side 31) brug et stort tal, og 
    sørg for at kun heltal under denne værdi optræder i input. Alternativt 
    (og bedre, da man undg˚ar at skulle tage hensyn til værdien valgt som 1),
    brug til Merge din pseudokode fra øvelse 2.3-2 (fra seddel med opgaver til uge 7), som ikke anvender 1.1

    JEG BENYTTER HER ALGORITMEN FRA BOGEN DATA-STRUCTURES AND ALGORITHMS IN PYTON, DEN ER MERE INTUITIV. SE s. 543
    parameters
    A: Det oprindelige array
    L: Venstre side af arrayet
    R: Højre side af arrayet
    """
    r = 0 # Right index
    l = 0 # left index
    while l + r < len(A):
        if r == len(R) or (l < len(L) and L[l] <= R[r]):
            A[l + r] = L[l]
            l += 1
        elif r < len(R):
            A[l + r] = R[r]
            r += 1
        
def merge_sort(A):
    n = len(A)
    if n < 2: # Vi tester altså om der er mindre end to elementer (altså 1 eller 0), da vi derved har ramt bunden i sorteringen og recursionen
        return
    # --- Divide ---
    mid = n//2 # Mid index
    L = A[:mid] # Left side
    R = A[mid:] # Right side
    
    # --- conquer ---
    merge_sort(L)
    merge_sort(R) 
    
    # --- combine ---
    merge(A,L,R)


# Opgave 2
"""
Tilføj tidtagning af din kode. Du skal kun tage tid p˚a selve sorteringen,
ikke den del af programmet som genererer array’ets/listens indhold.
Kør derefter din kode med input, som er tilfældige heltal. 
"""                
A = [randint(0,45) for i in range(20000)]
B = [randint(0,45) for i in range(100000)]
C = [randint(0,45) for i in range(200000)] 
D = [randint(0,45) for i in range(400000)] 
E = [randint(0,45) for i in range(800000)] 
lister = [A,B,C,D, E]

results_1 = []
for i in lister:
    start_time = time()
    merge_sort(i)
    end_time = time()
    results_1.append((time() - start_time) * 1000)

results_2 = []
for i in lister:
    start_time = time()
    merge_sort(i)
    end_time = time()
    results_2.append((time() - start_time) * 1000)

results_3 = []
for i in lister:
    start_time = time()
    merge_sort(i)
    end_time = time()
    results_3.append((time() - start_time) * 1000)

results = [mean([results_1[0], results_2[0], results_3[0]]),
           mean([results_1[1], results_2[1], results_3[1]]),
           mean([results_1[2], results_2[2], results_3[2]]),
           mean([results_1[3], results_2[3], results_3[3]]),
           mean([results_1[4], results_2[4], results_3[4]])]
print(results)
A = [randint(0,45) for i in range(20000)]
B = [randint(0,45) for i in range(100000)]
C = [randint(0,45) for i in range(200000)] 
D = [randint(0,45) for i in range(400000)] 
E = [randint(0,45) for i in range(800000)] 

results = [results[0]/20000 * log2(20000),
           results[1]/100000 * log2(100000),
           results[2]/200000 * log2(200000),
           results[3]/400000 * log2(400000),
           results[3]/800000 * log2(800000)]
print(results)