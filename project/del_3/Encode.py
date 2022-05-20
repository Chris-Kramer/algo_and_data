from Element import Element
import PQHeap as pqh
import DictBinTree as dbt
import sys
from bitIO import BitWriter, BitReader

# Open input and output files, using binary mode (reading/writing bytes)
infile = open(sys.argv[1], 'rb')
outfile = open(sys.argv[2], 'wb')

# Read each bit as an integer between 0 and 255
int_bits = []
while True:
    b = infile.read(1)
    if len(b) == 0:
        break
    int_bits.append(b[0])


# Create list of unique bits/integers (Used for counting frequencies)
u_vals = []
for int_bit in int_bits:
    if int_bit not in u_vals:
        u_vals.append(int_bit)


# Count frequencies
freqs = [0 for i in range(256)]
for u_val in u_vals:
    freq = int_bits.count(u_val)
    freqs[u_val] = freq


# HUFFMANN
def Huffman(C: list[int]):
    # Create pq
    Q = pqh.createEmptyPQ()
    # Convert frequencies to elements and place in pq
    for bit, freq in enumerate(C):
        c = Element(freq, bit)
        pqh.insert(Q,c)

    # Merge nodes
    for i in range(len(C) - 1):
        z_left = pqh.extractMin(Q)
        z_right = pqh.extractMin(Q)
        z_freq = z_left.key + z_right.key
        z_data = [z_left.data, z_right.data]
        z = Element(key = z_freq, data = z_data)
        pqh.insert(Q, z)
    return pqh.extractMin(Q)


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
    huffcode = ""
    _orderedTraversal(T,huffcode, return_list)
    return return_list


def _orderedTraversal(T: list,huffcode, return_list: list) -> None:
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
    if not isinstance(x, int) and len(x) > 1: 
        _orderedTraversal(x[0], huffcode, return_list)
        huffcode = huffcode + "0"
        _orderedTraversal(x[1],huffcode, return_list)
        huffcode = huffcode + "1"
    return_list.append(huffcode)


Q = Huffman(freqs)
huff_codes = orderedTraversal(Q.data)


bitWriter = BitWriter(outfile)
bitreader = BitReader(infile)
int_bits = []
while True:
    x = bitreader.readbit()
    print(x)
    if not bitreader.readsucces():  # End-of-file?
        break
