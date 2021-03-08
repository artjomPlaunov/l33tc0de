/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func getLen(head *ListNode) int {
    res := 0
    for head != nil {
        res += 1
        head = head.Next
    }
    return res
}

func aux(headA, headB *ListNode, lenA, lenB int) *ListNode {
    if lenA > lenB {
        return aux(headA.Next, headB, lenA-1, lenB)
    } else if lenB > lenA {
        return aux(headA, headB.Next, lenA, lenB-1)
    } else if headA == nil && headB == nil {
        return nil
    } else {
        if headA == headB {
            return headA
        } else {
            return aux(headA.Next, headB.Next, lenA-1, lenB-1)
        }
    }  
}

func getIntersectionNode(headA, headB *ListNode) *ListNode {
    lenA := getLen(headA)
    lenB := getLen(headB)
    return aux(headA, headB, lenA, lenB)
}
