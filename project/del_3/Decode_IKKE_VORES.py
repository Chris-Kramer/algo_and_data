"""
@author:        
    name:       Jannik Mangabat Bach Sørensen
    mail:       jsoer21@student.sdu.dk
    study nr:   194169
    
    name:       Merete Hansen   
    mail:       merha13@student.sdu.dk                                                      
    study nr:   129294 

    name:       Simon Thor Danielsen
    mail:       sidan21@student.sdu.dk
    study nr:   192926  
"""
import PQHeap
from Element import Element
import bitIO
import sys

# The input file
input_name = sys.argv[1]
# The output file
output_name = sys.argv[2]


def the_decode(path,output_path):
    frequency_reader = [0]*256 # Allocate memmory for the frequency list 
    
    with open(path, mode = "rb") as file_object: # Open file in binary mode
        with bitIO.BitReader(file_object) as file_object_encoded: # Open file as Bitreader
            
            # The frequency list is read by the readint32bits
            for a in range(256) :
                frequency_reader[a] = file_object_encoded.readint32bits()
        
        # The huffman tree is create to decorde the file
        huff_tree = huffman(frequency_reader)
        
        length = sum(frequency_reader) # The maximum number of characters needed to read the whole file
        
        with open(output_path, mode = 'wb') as file_writer: # A new file is open and the wrting can begin
            
            # The loop runs for all the needed characters 
            for _i in range(length):
                
                # A new huffman tree is saved as to not ruin the original tree when moving down the tree
                huffmann_depth = huff_tree.data[:] 
                
                # Loop runs as long as we are not a a leaf (int)
                while not isinstance(huffmann_depth, int):
                    bit = file_object_encoded.readbit() # The bit is read
                    huffmann_depth = huffmann_depth[bit] # A path is choosen 
                
                # The character is added to the file
                file_writer.write(bytes([huffmann_depth]))
                
            
# The same as in the encoder as this is the backbone of the file compression
def huffman(characters : list):
    min_priority_queue = PQHeap.createEmptyPQ() 
    
    for data, key in enumerate(characters):
        stuff = Element(key, data)
        PQHeap.insert(min_priority_queue, stuff)


    for _i in range(len(min_priority_queue) - 1):
            x_left_child = PQHeap.extractMin(min_priority_queue) 
            y_right_child = PQHeap.extractMin(min_priority_queue)

            frequency = x_left_child.key +  y_right_child.key
            
            z = Element(key = frequency, data = [x_left_child.data, y_right_child.data])
            PQHeap.insert(min_priority_queue, z)

    return PQHeap.extractMin(min_priority_queue)

the_decode(input_name,output_name)

