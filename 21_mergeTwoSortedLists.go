/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    aux := &ListNode{-1,nil}
    next := aux
    l, r := l1, l2
    
    for l != nil && r != nil {
        if l.Val < r.Val {
            next.Next = l
            l = l.Next
        } else {
            next.Next = r
            r = r.Next
        }
        next = next.Next
        next.Next = nil
    }
    if l != nil {
        next.Next = l
    } 
    if r != nil {
        next.Next = r
    }
    return aux.Next
}
