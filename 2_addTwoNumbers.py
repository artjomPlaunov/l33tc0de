# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode()
        cur = res
        carry = 0
        
        while l1 and l2:
            sum = l1.val + l2.val + carry
            cur.next = ListNode(sum%10)
            carry = sum//10
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        
        l = l1 if l1 else l2
        while l:
            sum = l.val + carry
            cur.next = ListNode(sum%10)
            carry = sum//10
            cur = cur.next
            l = l.next
        
        if carry:
            cur.next = ListNode(1)
        return res.next
        
