from typing import Any
import random
'''
Algoritmer og Datastrukturer | Projekt Del I
Gruppemedlemmer:
@ Andreas Lykke Nielsen | Eksamensnr.: 4102220
@ Christoffer Mondrup Kramer | Eksamensnr.: 4102366
'''

# Creates an empty Priority Queue
from typing import Any


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

def _get_left_child(i: int) -> int:
    """
    Returns the index of the left child

    Parameters
    ------------
    i: The index of the current node

    Return
    -----------
    An integer corresponding to the index of the left child
    """
    return (2 * i) + 1

def _get_right_child(i: int) -> int:
    """
    Returns the index of the right child

    Parameters
    ------------
    i: The index of the current node

    Return
    -----------
    An integer corresponding to the index of the right child
    """
    return (2 * i ) + 2

def _get_parent(i: int) -> int:
    """
    Returns the index of the parent of the node

    Parameters
    ------------
    i: The index of the current node

    Return
    -----------
    An integer corresponding to the index of the parent
    """
    return (i - 1)//2

def _exchange(i: Any, j: Any ) -> tuple[Any, Any]:
    """
    Exchanges two variables

    Parameters
    -----------
    i: Variable to be exchanged
    j: Variable to be exchanged

    Return
    -------
    Returns a tuple with the two variables exchanged

    Example:
    ---------
    >>> x = "x"
    >>> y = "y"
    >>> x, y = _exchange(x, y)
    >>> print(x)
    y
    >>> print(y)
    x
    """
    return (j, i)
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
    left = _get_left_child(index)
    right = _get_right_child(index)

    if left < heap_size and A[left] < A[index]:
        smallest = left
    else:
        smallest = index
    if right < heap_size and A[right] < A[smallest]:
        smallest = right
    if smallest != index:
        A[index], A[smallest] = _exchange(A[index], A[smallest])
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
    parent = _get_parent(i)
    while i > 0 and A[parent] > A[i]:
        A[i], A[parent] = _exchange(A[i], A[parent])
        i = A.index(A[parent])
        parent = _get_parent(i)