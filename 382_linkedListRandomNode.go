import "math/rand"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
type Solution struct {
    lst []int
}


/** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
func Constructor(head *ListNode) Solution {
    res := make([]int,0)
    for head != nil {
        res = append(res, head.Val)
        head = head.Next
    }
    return Solution{res}
}


/** Returns a random node's value. */
func (this *Solution) GetRandom() int {
    pick := rand.Intn(len(this.lst))
    return this.lst[pick]
}


/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(head);
 * param_1 := obj.GetRandom();
 */
