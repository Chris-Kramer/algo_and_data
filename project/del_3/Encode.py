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

# Count frequencies
freqs = [0 for i in range(256)]
for int_bit in int_bits:
    freq = int_bits.count(int_bit)
    freqs[int_bit] = freq

# Print Results
print()
print("Frequencies: " + str(freqs))
print("Length: " + str(len(freqs)))
print()


# ------------------ HUFFMANN --------------------------
Q = pqh.createEmptyPQ()
for freq in freqs:
    pqh.insert(Q,freq)

def Huffman(C):
    # Create priority que
    Q = pqh.createEmptyPQ()
    for c in C:
        pqh.insert(Q,c)
    
    # Merge nodes
    for i in Q:
        z_left= pqh.extractMin(Q)
        z_right = pqh.extractMin(Q)
        z_freq = z_left + z_right
        pqh.insert(Q, z_freq)
        #print(Q)
    print()
    print("ORDERED PQ: " + str(Q))
    print("Length: " + str(len(Q)))
    print()
Huffman(freqs)