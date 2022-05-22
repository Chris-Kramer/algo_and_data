'''
Algoritmer og Datastrukturer | Projekt Del III
Fil: Huffman.py
Gruppemedlemmer:
@Andreas Lykke Nielsen | Eksamensnr.: 4102220
@Christoffer Mondrup Kramer | Eksamensnr.: 4102366
'''

from typing import List
from Element import Element
import PQHeap as pqh

def Huffman(C: list[int]) -> list["Element"]:
    """
    -----------------
    Description
    -----------------
    A function which creates a huffmann tree.

    -----------------
    Parameters
    -----------------
    C: A list of frequencies (integers).
    
    -----------------
    Return
    -----------------
    An instance of the classe Element, hvis contains a Huffman Tree.
    """
    n = len(C)
    # Create pq
    Q = pqh.createEmptyPQ()
    # Convert frequencies to elements and place in pq
    for bit, freq in enumerate(C):
        c = Element(freq, bit)
        pqh.insert(Q,c)

    # Merge nodes
    for i in range(n - 1): # Minus 1 since we can't merge, when there is only one node left
        z_left = pqh.extractMin(Q)
        z_right = pqh.extractMin(Q)
        z_freq = z_left.key + z_right.key
        z_data = [z_left.data, z_right.data]
        z = Element(key = z_freq, data = z_data)
        pqh.insert(Q, z)   
    return pqh.extractMin(Q)


def generate_huffcodes(T: list[int]) -> list[str]:
    """
    -----------------
    Description
    -----------------
    A function which loops through Huffman Tree and generates huffcodes.

    -----------------
    Parameters
    -----------------
    T: A huffman tree.
    n_char: How many characters are used in the decoding?
        - This is the length of the table of freqencies

    -----------------
    Preconditions
    -----------------
    T must be represented as nested lists.
        - A leaf is an integer
        - An inner node is lit containing two elements
        
    -----------------
    Return
    -----------------
    A list containing huffcodes corresponding to integers between 0 and 256
    """
    huff_codes = [""] * 256
    _generate_huffcodes(T, "", huff_codes)
    return huff_codes


def _generate_huffcodes(T: list[int], huffcode: str, huff_codes: list[str]) -> None:
    """
    -----------------
    Description
    -----------------
    An internal function which handles recursive calls for huffcode generation

    -----------------
    Parameters
    -----------------
    T: A huffman tree.
    huffcode: A parameter used for concatenating 0 and 1 through recursion

    -----------------
    Preconditions
    -----------------
    T must be represented as nested lists.
        - A leaf is an integer
        - An inner node is lit containing two elements
    """
    if not isinstance(T, int) and len(T) > 1:
        _generate_huffcodes(T[0], huffcode + "0", huff_codes)
        _generate_huffcodes(T[1], huffcode + "1", huff_codes)
    else: #Found leaf
        huff_codes[T] = huffcode