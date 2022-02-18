from cmath import inf
from math import floor
from random import randint


def merge(A: list[int], p:int, q: int, r:int) -> None:
    """
    Implementer Mergesort i Java eller Python ud fra bogens pseudokode
    (side 31 og 34). Lad input være et array (Java) eller liste (Python) 
    af heltal. Som værdien 1 (pseudokode side 31) brug et stort tal, og 
    sørg for at kun heltal under denne værdi optræder i input. Alternativt 
    (og bedre, da man undg˚ar at skulle tage hensyn til værdien valgt som 1), brug til Merge din pseudokode fra øvelse 2.3-2 (fra seddel med
    opgaver til uge 7), som ikke anvender 1.1
    """

    r = len(A) - 1 # Last index
      
    L = A[p + 1:] # Left array
    R = A[q:] # Right array
    
    l_sentinel = max(L)
    r_sentinel = max(R)
    # For at undgå sentinels kan man benytte en while-løkke
    j = 0 # Right index
    
    for i in range(len(A) - 1):
        if L[i] <= R[j] and L[i] ! :
            A[i] = L[i] 
        elif A[i] == R[j] and str(R[j]) != "NA":
            j += 1

def merge_sort(A, p, r):
    if p < r:
        q = floor((p + r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
                
A = [randint(0,49) for i in range(10)]
print(A)
merge_sort(A,0, len(A) - 1 )
print(A)