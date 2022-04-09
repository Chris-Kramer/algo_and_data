def createEmptyDict() -> None:
    """
    Returns an empty binary tree
    """
    return [None]


def search(T: list, k: int) -> bool:
    """
    Returns a bool indicating if the key is present in the Tree
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
    Inserts a node with a key in the binDictTree
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
        #T.append([k,None,None])
        T.append([k, None, None])
        
        #T[0] = k
        #T.append(None)
        #T.append(None)
    elif k < y[0]:
        y[1] = k
    else:
        y[2] = k


def orderedTraversal(T: list) -> list:
    """
    Returns an ordered list of the binary tree. This is a public function, which passes the relevant parameters to the internal and private function
    """
    return_list = []
    _orderedTraversal(T[0], return_list)
    return return_list

def _orderedTraversal(T: list, return_list: list) -> None:
    """
    An internal function, which handles the recursive calls
    """ 
    x = T
    if x is not None:
        _orderedTraversal(x[1], return_list)
        return_list.append(x[0])
        _orderedTraversal(x[2], return_list)      

if __name__ == "__main__":
    #T = [[5,[2, None, None], [8, None,[11,None,None]]]]
    #T = [[5,[2, None, None], [8, None, None]]]
    #T = createEmptyDict()
    #print(orderedTraversal(T))
    #print(search(T, 8))
    
    #Test insert
    T = createEmptyDict()
    print(T)
    insert(T,9)
    print(T)
    insert(T,12)
    #insert(T,7)
    print(T)
    
    


