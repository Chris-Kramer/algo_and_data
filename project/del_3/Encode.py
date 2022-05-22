'''
Algoritmer og Datastrukturer | Projekt Del III
Fil: Encode.py
Gruppemedlemmer:
@Andreas Lykke Nielsen | Eksamensnr.: 4102220
@Christoffer Mondrup Kramer | Eksamensnr.: 4102366
'''
import sys
from bitIO import BitWriter
from Huffman import Huffman, generate_huffcodes
# Files
infile = sys.argv[1] 
outfile = open(sys.argv[2], "wb")


###### CREATE LIST OF FREQUENCIES ######
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
        
######## GENERATING HUFFMANN TREE AND CODES ########
huffTree = Huffman(freqs)
huff_codes = generate_huffcodes(huffTree.data)

####### WRITE TO OUTPUT ##########
with open(infile, mode = "rb") as fileReader: 
    bitWriter = BitWriter(outfile)
    
    # Write frequncies to output file
    for freq in freqs:                     
        bitWriter.writeint32bits(freq)
    
    # Read bit for bit and write to output file
    while True:
        b = fileReader.read(1)
        if len(b) == 0:
            break
        huff_code = huff_codes[b[0]]
        for bit in huff_code:
            bitWriter.writebit(int(bit))
outfile.close() 