'''
Algoritmer og Datastrukturer | Projekt Del III
Fil: Decode.py
Gruppemedlemmer:
@Andreas Lykke Nielsen | Eksamensnr.: 4102220
@Christoffer Mondrup Kramer | Eksamensnr.: 4102366
'''
import sys
from bitIO import BitReader, BitWriter
from Huffman import Huffman

# Open files and create bitwriters/readers
infile = open(sys.argv[1], "rb")
outfile = open(sys.argv[2], "wb")
bitWriter = BitWriter(outfile)
bitReader = BitReader(infile)

###### CREATE LIST OF FREQUENCIES ######
freqs = []
for i in range(256):
    b = bitReader.readint32bits()
    freqs.append(b)
    
######## GENERATE HUFFMANN TREE ########
huffTree = Huffman(freqs)

######## WRITE TO OUTPUT ######## 
total_bytes = sum(freqs)
for i in range(total_bytes):
    temp_Tree = huffTree.data
    while not isinstance(temp_Tree, int):
        x = bitReader.readbit()
        temp_Tree = temp_Tree[x]
    outfile.write(bytes([temp_Tree]))
outfile.close()
infile.close()