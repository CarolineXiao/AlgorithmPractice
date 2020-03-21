import random

class RandomizedSet:
    
    def __init__(self):
        self.random_set = []
        self.value_to_index = {}
        self.index = 0

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        if val in self.value_to_index:
            return False
        self.random_set.append(val)
        self.value_to_index[val] = self.index
        self.index += 1
        return True
        
        

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        if val not in self.value_to_index:
            return False
        pos = self.value_to_index[val]
        if pos == self.index-1:
            del self.value_to_index[val]
            self.random_set.pop()
            self.index -= 1
            return True
        last_value = self.random_set[self.index-1]
        self.random_set[self.index-1], self.random_set[pos] = self.random_set[pos], self.random_set[self.index-1]
        self.value_to_index[last_value] = pos
        del self.value_to_index[val]
        self.random_set.pop()
        self.index -= 1
        return True
        

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        
        return self.random_set[random.randrange(0, self.index)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
