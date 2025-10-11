"""
LRU Cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement the LRUCache class:
LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.


remove
head --> node --> tail
next, prev = node.next, node.prev
next.prev, prev.next = prev, next

add to front
head --> node1 --> node2 --> node3 --> tail

"""

class Node:
    def __init__(self, key, val):
        self.val = val
        self.key =  key
        self.prev = self.next = None
        
class lRUCache:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self.cache = {}
        self.head = self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _remove(self, node: Node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        
    def _add_to_front(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        
    def get(self, key:int):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add_to_front(node)
            return node.val
        return -1
    
    def put(self, key:int, val: int) -> None:
        node = Node(key, val)
        
        if key in self.cache:
            self._remove(self.cache[key])
        self._add_to_front(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]   
        