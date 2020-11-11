from collections import defaultdict

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return head
        
        oldPointerMap = {}
        newPointerMap = {}
        
        ptr     = head
        i       = 0
        newHead = Node(0)
        curr    = newHead
        idPtrMap = {}
        while ptr is not None:
            oldPointerMap[id(ptr)] = i
            curr.next = Node(ptr.val)
            curr = curr.next
            idPtrMap[id(curr)] = curr
            idPtrMap[id(ptr)] = ptr
            newPointerMap[i] = id(curr) 
            i += 1
            ptr = ptr.next
        
        ptr = newHead.next
        oldPtr = head
        
        print(oldPointerMap, newPointerMap)
        
        while ptr is not None:
            if oldPtr.random:
                ptr.random = idPtrMap[newPointerMap[oldPointerMap[id(oldPtr.random)]]]
            else:
                ptr.random = None
            oldPtr = oldPtr.next
            ptr = ptr.next
           
        return newHead.next
        
        
