import sys
import DictBinTree as dbt

T = dbt.createEmptyDict()
n = 0
for line in sys.stdin:
    dbt.insert(T,int(line))
    print(T)
    n += 1

sorted_list = dbt.orderedTraversal(T)

for element in sorted_list:
    print(element)