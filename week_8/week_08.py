"""
I.B 
1.
Implementer Quicksort i Java eller Python ud fra bogens pseudokode
(side 171). Test at din kode fungerer ved at generere arrays med forskelligt indhold og sortere dem.
Tilføj tidstagning af din kode 
(kun selve sorteringen, ikke den del af programmet som genererer arrayets
indhold).
"""

from cmath import inf
from random import randint
import math
from statistics import mean
from time import time


def partition(A: int, p: int, r: int) -> int:
    x = A[r]
    i = - 1 
    for j in range(r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i] # Swap elements (Place A[j] at the end of the lower partition)
    A[i + 1], A[r] = A[r], A[i + 1] #Swap first and last elements
    return i + 1

def quicksort(A: int, p: int, r: int) -> float:
    if p < r:
        q = partition(A, p, r)
        quicksort(A,p, q - 1) # Left side
        quicksort(A, q + 1, r) # Right side


"""
Har ikke lavet den helt færdig, men testede blot med nogle stykker, tallene er konstante. 

Kør derefter din kode med input, som er random ints. Gør dette for mindst 5 forskellige værdier af n (antal elementer at sortere),
vælg værdier som får programmet til at bruge fra ca. 100 til ca. 5000 millisekunder. 
Gentag hver enkelt kørsel tre gange og find gennemsnittet af antal millisekunder brugt ved de tre kørsler.
Divider de fremkomne tal med n log2 n og check derved hvor godt analysen passer med praksis
de resulterende tal burde ifølge analysen være konstante
"""
A = [randint(0, 30) for i in range(10)]
B = [randint(0, 30) for i in range(100)]
C = [randint(0, 30) for i in range(1000)]
D = [randint(0, 30) for i in range(10000)]
E = [randint(0, 30) for i in range(10000)]

start_time = time()
quicksort(D, 0, len(D) - 1)
res = (time() - start_time)*1000
print(res / len(D)*math.log2(len(D)))


def test_heap(A):
    A.insert(0,inf)
    for i in range(2,len(A)):
        parent = i//2
        right_child = 2*i + 1
        left_child = 2*i
        print(f"Current node: {A[i]}")
        print(f"Parent is {A[parent]} which is {A[i] <= A[parent]}")
        print(f"Right child is {A[right_child]} which is {A[i] >= A[right_child]}")
        print(f"Left child is {A[left_child]} which is {A[i] >= A[left_child]}")

test_heap([23,17,14,6,13,10,1,5,7,12])