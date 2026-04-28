class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node
        
        # left=lru right=most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        # want them to initially be connected
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node) -> None:
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
