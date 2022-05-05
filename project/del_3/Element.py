from functools import total_ordering

@total_ordering
class Element:

    def __init__(self,key,data):
        self.key = key
        self.data = data

    def __eq__(self,other):
        return self.key == other.key

    def __lt__(self,other):
        return self.key < other.key
    
    def __str__(self):
        return f"Key: {self.key}, data: {self.data}"
        
    def __repr__(self):
        return f"Key: {self.key}, data: {self.data}"