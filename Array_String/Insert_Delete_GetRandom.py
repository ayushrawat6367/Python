import random

class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        # Move the last element to the place of the element to delete
        last_element = self.vals[-1]
        idx_to_replace = self.val_to_index[val]
        self.vals[idx_to_replace] = last_element
        self.val_to_index[last_element] = idx_to_replace
        # Remove the last element
        self.vals.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)


#########Example

obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(2)
param_3 = obj.insert(2)
param_4 = obj.getRandom()
param_5 = obj.remove(1)
param_6 = obj.insert(2)
param_7 = obj.getRandom()
