from Element import Element
import PQHeap as pqh
import DictBinTree as dbt
import sys

# Open input and output files, using binary mode (reading/writing bytes).
infile = open(sys.argv[1], 'rb')
outfile = open(sys.argv[2], 'wb')

# Read each bit
int_bits = []
while True:
    b = infile.read(1)
    if len(b) == 0:
        break
    int_bits.append(b[0])

# Create list of unique values
u_vals = []
for int_bit in int_bits:
    if int_bit not in u_vals:
        u_vals.append(int_bit)
        
# Count frequencies
freqs = [0 for i in range(256)]
for u_val in u_vals:
    freq = int_bits.count(u_val)
    freqs[u_val] = freq

# COnvert to elements
elements = []
for i, freq in enumerate(freqs):
    e = Element(key = freq, data = i)
    elements.append(e)
    
    
# ------------------ HUFFMANN --------------------------
Q = pqh.createEmptyPQ()
for freq in freqs:
    pqh.insert(Q,freq)

def Huffman(C: list["Element"]):
    # Create priority que
    Q = pqh.createEmptyPQ()
    for bit, freq in enumerate(C):
        c = Element(freq, bit)
        pqh.insert(Q,c)
    # Merge nodes
    for i in Q:
        z_left= pqh.extractMin(Q)
        z_right = pqh.extractMin(Q)
        z_freq = z_left.key + z_right.key
        sub_T = [[z_left.data], [z_right.data]]
        print(sub_T)
        z = Element(key = z_freq, data = sub_T)
        pqh.insert(Q, z)
    return Q

freqs = [5, 9, 12, 13, 16, 45]
Q = Huffman(freqs)

# THIS SHOULDN'T WORK, BUT IT DOES
for q in Q:
    z_left= pqh.extractMin(Q)
    z_right = pqh.extractMin(Q)
    z_freq = z_left.key + z_right.key
    z_data = [[z_left.data], [z_right.data]]
    z = Element(key= z_freq, data = z_data)
    pqh.insert(Q, z)

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
    _orderedTraversal(T, return_list)
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
    if not isinstance(x, int):
        _orderedTraversal(x[0], return_list)
        if len(x) == 1:
            print(f"INNER: {x[0]}")
        else:
            _orderedTraversal(x[1], return_list)


Q = [Element(key = 6500, data= [[[97],[98]],[99]])]
print(Q)
print()
test = orderedTraversal(Q[0].data)