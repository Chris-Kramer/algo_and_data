from audioop import reverse
from curses import KEY_A1
from math import ceil, floor
from time import time
from random import shuffle
from random import randint
from typing import Optional
def selection_sort(A):
    """
    P. 29 cormen et al. exercise 2.2
    """
    # at least n - 1 operations
    op = 0
    for i in range(len(A) - 1): # We don't need to sort the last element, it so minus
        current_value = A[i]
        smallest_i = i
        # at least n - 2 operations
        for j in range(i + 1, len(A)):
            op += 1
            if A[j] < A[smallest_i]:
                smallest_i = j

        A[i] = A[smallest_i]
        A[smallest_i] = current_value
    # Since we have n two times, the running time is n**2    

# Implementation
#A = [randint(0,12) for i in range(10)]
#shuffle(A)
#print(A)
#selection_sort(A)
#print(A)

def linear_search(A, v):
    """
    P. 29 cormen et al. exercise 2.3
    """
    result = None
    i = 0
    #Max n operations never more, that is worst case of linear
    while i <= len(A) - 1 and result is None: 
        if A[i] == v:
            result = v
        i = i + 1
    return result

# Implementation:
#A = [i for i in range(3)]
#print(A)
#print("rest:" + str(linear_search(A, 1)))


def insertionSort(A: list[int]) -> int:
    """
    Implementer InsertionSort i Java eller Python ud fra pseudo-koden side 18 i lærebogen. 
    """
    start_time = time()
    for j in range(1,len(A)): # Current Index
        key = A[j] #Current value
        i = j - 1 #Previous index 
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    end_time = time()
    return end_time - start_time

# Test implementation
"""
A = [i for i in range(1000)]
best_case = insertionSort(A)
A.reverse()
worst_case = insertionSort(A)
print(f"Best case: {best_case}, Worst case: {worst_case}")
"""
def  naive_pol_eval(A: list[int], x) -> None:
    """
    Naive polunomial evaluation
    """
    res = 0
    for i in range(len(A)): # Always n times  
        p = 1
        for j in range(i): #At least n times
            p = p * x
        res += A[i]*p
    print("Result: " + str(res))
    # Run time = n**2
#A = [i for i in range(10)]
#
# naive_pol_eval(A, 3)

def binary_search(A: list[int], v: int) -> Optional[int]:
    """
    Cormen et al. øvelse 2.3-5 (side 39). Udvid opgaven således:
    Start med at illustrere algoritmen med en tegning. Lav derefter pseudokode 
    for algoritmen (som i opgaveteksten). Lav derefter et program i Java 
    eller Python på basis af din pseudokode. Test til sidst korrekthed af 
    din implementation ved at generere arrays (Java) eller lister (Python)
    """
    print(A)
    middle = floor((len(A)/2))
    print(middle)

    if A[middle] < v and len(A) > 1:
        A = A[middle:] #
        return binary_search(A, v)

    elif A[middle] > v and len(A) > 1:
        A = A[: middle]
        return binary_search(A, v)
    
    elif A[middle] == v:
        return middle
    
    else:
        return None

#Test implementation
"""
A = list(range(0, 100000, 35))
print(binary_search(A, 451))
"""

def insertionSortBinary(A: list[int]) -> int:
    """
    Implementer InsertionSort med binær søgning fremfor linær
    """
    for j in range(1,len(A)): # Current Index
        key = A[j] #Current value
        i = j - 1 #Previous index
        print(f"KEY {key}, i {i}")
        
        something = False
        A_search = A[:j]
        while len(A_search) > 1:
            middle = floor(len(A_search)/2)
            
            if A[middle] < key:
                A_search = A_search[middle + 1:]
            
            elif A[middle] == key:
                #Switch and current
                A[i + 1] = A[i] 
            
            elif A[middle] > key:
                A_search = A_search[:middle - 1]


            else:
                return None  

        A[i + 1] = key


A = list(range(0, 10))
shuffle(A)
print(A)
insertionSortBinary(A)