# https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.leftPointer = Node(0, 0, None, None)
        self.rightPointer = Node(0, 0, None, None)

        self.leftPointer.next = self.rightPointer
        self.rightPointer.prev = self.leftPointer

        self.capacity = capacity
        self.currentSize = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        targetNode = self.cache[key]
        self.put(targetNode.key, targetNode.val)

        return targetNode.val
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
            self.currentSize -= 1

        if self.currentSize == self.capacity:
            del self.cache[self.leftPointer.next.key]
            self.remove(self.leftPointer.next)
            self.currentSize -= 1
            
        next = self.rightPointer
        prev = next.prev

        insertNode = Node(key, value, prev, next)
        prev.next = insertNode
        next.prev = insertNode
        
        self.cache[key] = insertNode
        self.currentSize += 1

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev