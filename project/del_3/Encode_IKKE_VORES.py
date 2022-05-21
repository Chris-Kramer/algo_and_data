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
from Element import Element
import PQHeap
import bitIO

#encoding(input_path + "\\same.txt", output_path + "\\same_encoded.txt")
# The input file
input_name = "test.txt"
#sys.argv[1]
# The output file
output_name = 'results'

#sys.argv[2]

def frequency_table(path):
    with open(path, mode = "rb") as file_object:  # Opens up file in bit reading mode
        counter = [0] * 256                       # Creates an empty list from 0-256
        byte = file_object.read(1)                # Readeing 1 byte
        while byte:
            counter[byte[0]] += 1
            byte = file_object.read(1)
    return counter

def huffman(characters : list()):
    min_priority_queue = PQHeap.createEmptyPQ()   # The root of our huffmantree
    
    # Data is our ASCII code for interpretation. key is our frequency 
    for data, key in enumerate(characters): 
        stuff = Element(key, data)
        PQHeap.insert(min_priority_queue, stuff) # Inserting key and data into the tree

    # The loop iterates through the entiere queue
    for _i in range(len(min_priority_queue) - 1):
        
        # The left and right child is extracted
        x_left_child = PQHeap.extractMin(min_priority_queue) 
        y_right_child = PQHeap.extractMin(min_priority_queue)
        
        # The frequency og the node is found 
        frequency = x_left_child.key +  y_right_child.key 
        
        # The new element is merged to contain the childred with the addede frequency
        z = Element(key = frequency, data = [x_left_child.data, y_right_child.data]) ## combines our frequency with 
        
        # The new element is added to our queue and there fore reduseing it by one 
        PQHeap.insert(min_priority_queue, z)
    
    # The root of the tree is retuned 
    q = PQHeap.extractMin(min_priority_queue)
    return q

def create_huffmann_path_codes(node, path = ""): ## Inorder treewalk
    binary_path_codes = dict()  # Dictiotionary for storage of each binary path

    if not isinstance(node, int):
        binary_path_codes.update(create_huffmann_path_codes(node[0], path + "0")) # Left turns with 0       

        binary_path_codes.update(create_huffmann_path_codes(node[1], path + "1")) # Right turns with 1
    else:
        binary_path_codes[node] = path # Saves the keyword for our character  
    
    # Return the dictnary of keywords and characters
    
    return binary_path_codes

def encoding(input_path, output_path):
    # Stores the generated frequency table
    frequency = frequency_table(input_path)
    # Creates the huffmantree from the frequency table.
    huffmantree = huffman(frequency) 
    # Generate huffmann binary codes from the huffmantree with the use of the huffmantree.
    huffman_code_map = create_huffmann_path_codes(huffmantree.data)
    huffman_code_map[49]
    with open(input_path, mode = "rb") as file_reader:  # Opens up file in bit reading mode
        byte = file_reader.read(1)       # Readeing 1 byte
        
        with open(output_path, mode = 'wb') as file_writer: # Opens up file in writing mode
            with bitIO.BitWriter(file_writer) as binary_writer: # Opens up file in bit wrting mode
                
                # Insert all frequencies at the top of the file for easier reading
                for keys in frequency:                     
                    # It is written in non-encoded bits 
                    binary_writer.writeint32bits(keys)
                    
                # The loop iterateas as long as there is bits to be read
                i = 0
                print("DERES")
                while byte:
                    # The byte is used to find the keyword for the encoding
                    huffman_binary_path = huffman_code_map[byte[0]]
                    
                    if i == 50:
                        break
                    i += 1
                    # Loops over all the 1's and 0's in the encoding 
                    for char in huffman_binary_path:
                        
                        # The bit encoding is writting into the file
                        print(char, end="") 
                        binary_writer.writebit(int(char))
                    
                    # A new byte is read
                    byte = file_reader.read(1)

# The activation comand 
encoding(input_name , output_name)



