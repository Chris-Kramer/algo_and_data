from itertools import cycle
from random import shuffle
from statistics import mean
import typing
from matplotlib import pyplot as plt


def rand_permutations(n: int) -> list[int]:
    """
    Lav et Java- eller Python-program,
    som genererer en tilfældig permutation af heltallene fra 0 til n−1 (for et n som er en input parameter).
    """
    temp = [i for i in range(n)]
    shuffle(temp)
    return temp

def count_cycles(perm_list: list[int]) -> int:
    """
    Counts how many cycles there exists in a permutation
    """

    cycles = 0 # Amount of cycles
    vals = [] # Values which are in a chain are added here
    for val in perm_list:

        # Move to next element in list, if the current value is already part of a larger chain
        if val in vals: # Very inefficient, but it gets the job done
            next

        else:
            vals.append(val) # Append current value to the list of value in a cycle 
            #(It will be part of the cycle since it always at least refers to itself)

            next_val = perm_list[val] # Get the value of the index corresponding to current cycle            
            while next_val != val: # Test if the next value in the cycle is it self 
                vals.append(next_val) # Next value is part of the cycle, so append it
                next_val = perm_list[next_val] # Get next value in the cycle
            
            cycles += 1  
    return cycles

def main():
    """
    I øvelsestimen lavede du et program, som kunne generere en tilfældig permutation, og et program, som kunne tælle antal kredse i en permutation.
    Brug disse programmer til at generere en masse tilfældige permutationer af længde 16, og tæl for hver af dem antallet af kredse i dem.
    Brug data fra disse kørsler til at give et bud p˚a sandsynligheden for, at der i en tilfældig permutation med n = 16 er k kredse, for k = 1; 2; : : : ; 16. Dvs. lav din egen version af figur 3 i noterne, men med n
    lig 16 og ikke 64. 
    Find også det gennemsnitlige antal kredse i dine eksperimenter. Passer dit tal med formlen p˚a side 4 i noterne,
    dvs. er det tæt på H16 =P16 i=1 1=i = 1=1 + 1=2 + 1=3 + : : : + 1=16?
    """
    cycles = [count_cycles(rand_permutations(16)) for i in range(1000000)]
    avg = mean(cycles)
    res = 0
    for i in range(1, 16 + 1):
        res += 1/i
    print(f"result: {res}, avg: {avg}")    

if __name__ == "__main__":
    main()
