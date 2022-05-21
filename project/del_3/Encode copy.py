"""
Encode.py
----------
@Created by:
    Navn : Andreas Lykke Nielsen
    studienr. : 

    Navn: Christoffer Mondrup Kramer
    studienr. : 
"""
from cmath import inf
from Element import Element
import PQHeap as pqh
import DictBinTree as dbt
import sys
from bitIO import BitWriter, BitReader

# HUFFMANN
def Huffman(C: list[int]):
    n = len(C)
    # Create pq
    Q = pqh.createEmptyPQ()
    # Convert frequencies to elements and place in pq
    for bit, freq in enumerate(C):
        c = Element(freq, bit)
        pqh.insert(Q,c)

    # Merge nodes
    for i in range(n - 1): #for q in Q:
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


return_list = []
def _orderedTraversal(T: list, huffcode: str) -> None:
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
        _orderedTraversal(x[0], huffcode + "0")
        _orderedTraversal(x[1], huffcode + "1")
    else: #Found leaf
        return_list.append(huffcode)
    #return return_list


# Open input and output files, using binary mode (reading/writing bytes)
infile = sys.argv[1]
outfile = sys.argv[2]

##### COUNT FREQS ################
with open(infile, "rb") as fileReader: 
# Read each bit as an integer between 0 and 255
    int_bits = []
    while True:
        b = fileReader.read(1)
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
        
######## HUFFF MAN #############
huffTree = Huffman(freqs)
huff_codes = _orderedTraversal(huffTree.data, "")
print(return_list[49])


####### WRITE OUTPUT ##########
with open(infile, mode = "rb") as file_reader:  # Opens up file in bit reading mode
    byte = file_reader.read(1)       # Readeing 1 byte
    
    with open(outfile, mode = 'wb') as file_writer: # Opens up file in writing mode
        with BitWriter(file_writer) as binary_writer: # Opens up file in bit wrting mode
            
            # Insert all frequencies at the top of the file for easier reading
            for freq in freqs:                     
                # It is written in non-encoded bits 
                binary_writer.writeint32bits(freq)
            # The loop iterateas as long as there is bits to be read
            
            i = 0
            while byte:
                # The byte is used to find the keyword for the encoding
                print(byte[0])
                huffman_binary_path = huff_codes[byte[0]]
                print(huffman_binary_path)
                if i == 10:
                    break
                # Loops over all the 1's and 0's in the encoding 
                for char in huffman_binary_path:
                    
                    # The bit encoding is writting into the file 
                    binary_writer.writebit(int(char))
                
                # A new byte is read
                byte = file_reader.read(1)

""""
with open(outfile, 'wb') as filewriter:
    with BitWriter(filewriter) as binarywriter:
            
        #Write frequencies to outfile
        for freq in freqs:
            binarywriter.writeint32bits(freq)
            
        #Write huffman codes to file
        with open(infile, "rb") as fileReader:
            while True:
                b = fileReader.read(1)
                if len(b) == 0:
                    break
                huff_code = huff_codes[b[0]]
                for bit in huff_code:
                    binarywriter.writebit(int(bit))
            
"""
#outfile.close()
