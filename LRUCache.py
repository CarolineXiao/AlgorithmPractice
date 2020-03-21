class cacheNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # linked list -> cache
        dummy = cacheNode(-1, -1)
        self.head = dummy
        self.end = dummy
        # hash map -> key to position in cache
        self.key_to_position = {}
        self.capacity = capacity
        self.size = 0

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.key_to_position:
            return -1

        value = self.key_to_position[key].next.val
        self.move2End(key, value)
        return value
        
    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # cache list not reaching capacity
        # key does not exist in cache
        if key in self.key_to_position:
            self.move2End(key, value)
            return

        self.key_to_position[key] = self.end
        new_node = cacheNode(key, value)
        self.end.next = new_node
        self.end = new_node
        
        if len(self.key_to_position) > self.capacity:
            # remove head node
            node = self.head.next
            if node.next != None:
                self.key_to_position[node.next.key] = self.head
            del self.key_to_position[node.key]
            self.head.next = node.next
            node.next = None
            
    def move2End(self, key, value):
        prev = self.key_to_position[key]
        cur = prev.next
        cur.val = value
        if cur == self.end:
            return
        
        self.key_to_position[cur.next.key] = prev
        prev.next = cur.next
        cur.next = None
        self.key_to_position[cur.key] = self.end
        self.end.next = cur
        self.end = cur
     
