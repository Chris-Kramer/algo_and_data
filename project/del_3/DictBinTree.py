#!/usr/bin/env python3
def createEmptyDict() -> list[None]:
    """
    -----------------
    Description
    -----------------
    Returns an empty binary tree
    
    -----------------
    Parameters
    -----------------
    None

    -----------------
    Return
    -----------------
    An empty binary tree, represented as a list containing a None object
    
    -----------------
    Preconditions
    -----------------
    None
    """
    return [None]


def search(T: list, k: int) -> bool:
    """
    ----------------
    Description
    ----------------
    Search for an integer value in a binary search Tree

    ----------------
    Parameters
    ----------------
    T: A binary search tree
    k: An integer to search for in the tree

    ---------------
    Return
    ---------------
    Returns a bool indicating if the key is present in the Tree

    ---------------
    Preconditions
    ---------------
    T must be represented as nested lists
    """
    x = T[0]
    while x is not None:
        if k == x[0]:
            return True
        elif k < x[0]:
            x = x[1]
        else: 
            x = x[2]
    return False


def insert(T: list, k: int) -> None:
    """
    -----------------
    Description
    -----------------
    Inserts a node with a key in a binary search tree
    
    -----------------
    Parameters
    -----------------
    T: A binary search tree
    k: An integer to search for in the tree

    -----------------
    Return
    -----------------
    None

    -----------------
    Preconditions
    -----------------
    T must be represented as nested lists
    """
    y = None
    x = T[0]
    while x is not None:
        y = x
        if k < x[0]:
            x = x[1]
        else:
            x = x[2]
    if y is None: # If it is an empty tree
        T[0] = [k, None, None]
    elif k < y[0]:
        y[1] = [k, None, None]
    else:
        y[2] = [k, None, None]


def orderedTraversal(T: list) -> list[int]:
    """
    -----------------
    Description
    -----------------
    Sort a binary search tree in increasing order.

    -----------------
    Parameters
    -----------------
    T: A binary search tree

    -----------------
    Return
    -----------------
    A list of integers sorted in increasing order

    -----------------
    Preconditions
    -----------------
    T must be represented as nested lists
    """
    return_list = []
    _orderedTraversal(T[0], return_list)
    return return_list

def _orderedTraversal(T: list, return_list: list) -> None:
    """
    -----------------
    Description
    -----------------
    An internal function, which handles the recursive calls for the public function orderedTraversal(T)

    -----------------
    Parameters
    -----------------
    T: A binary search tree
    return_list: The list which will be returned by the public function

    -----------------
    Preconditions
    -----------------
    T must be represented as nested lists
    return_list is empty first time this function is called (it will be populated through recursion)
    """ 
    x = T
    if x is not None:
        _orderedTraversal(x[1], return_list)
        return_list.append(x[0])
        _orderedTraversal(x[2], return_list)

