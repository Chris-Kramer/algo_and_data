import os
import sys

'''
Algoritmer og Datastrukturer | Projekt Del I
Gruppemedlemmer:
@ Andreas Lykke Nielsen | Eksamensnr.: 4102220
@ Christoffer Mondrup Kramer | Eksamensnr.: 4102366
'''

# Creates an empty Priority Queue
def createEmptyPQ() -> list:
    """
    Creates an empty priority queue
    
    Parameters
    ----------
    No parameters
    
    Return
    -------
    Empty list
    """
    return []


# Min heapifying algorithm.
def MinHeapify(A: list[int], index: int):
    """
    Takes an array and a user specified index from which the Min-Heapification will happen.

    Parameters
    ----------
    A: An array of integers
    
    Return
    ------
    No return value
    """
    heap_size = len(A)
    left = (2*index)+1 # Left child
    right = (2*index)+2 # Right child

    if left < heap_size and A[left] < A[index]:
        smallest = left
    else:
        smallest = index
    if right < heap_size and A[right] < A[smallest]:
        smallest = right
    if smallest != index:
        A[index], A[smallest] = A[smallest], A[index]
        MinHeapify(A,smallest) # Recursion
    

def extractMin(A: list) -> int:
    """
    Returns and removes the element with lowest priority (Root of the tree) from the heap

    Preconditions
    -------------
    The input must be a heap
    The heap must not be empty
    
    Parameters
    ----------
    A: A list, which is structured as a heap/priority queue
    
    Return
    ------
    The smallest integer in the heap
    
    """
    smallest = A[0]
    A[0] = A[-1]
    A.pop(-1)
    MinHeapify(A,0)
    return smallest

def insert(A: list, e: int) -> None:
    """
    Inserts an element into a heaps so it maintains its structure
    
    Parameters
    ----------
    A: An array, which follows the heap structure
    e: The integer, which will be inserted into the heap
    
    Preconditions
    -------------
    A must follow the Min heap structure
    e must be an integer
    
    Return
    ------
    No return value
    """ 
    i = len(A)
    A.append(e)
    parent = (i - 1)//2
    while i > 0 and A[parent].key > A[i].key:
        A[i], A[parent] = A[parent], A[i]
        i = A.index(A[parent])
        parent = (i - 1)//2
        