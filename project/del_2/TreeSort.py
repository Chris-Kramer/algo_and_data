#!/usr/bin/env python3 
import sys
import DictBinTree as dbt

def main():  
    T = dbt.createEmptyDict()
    n = 0
    for line in sys.stdin:
        dbt.insert(T,int(line))
        n += 1

    sorted_list = dbt.orderedTraversal(T)
    for element in sorted_list:
        print(element)

if __name__ == "__main__":
    main()