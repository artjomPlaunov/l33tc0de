/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type BSTIterator struct {
    Stack []*TreeNode
}


func Constructor(root *TreeNode) BSTIterator {
    stack := make([]*TreeNode,0)
    
    if root == nil {
        return BSTIterator{stack}    
    }
    cur := root
    for cur.Left != nil {
        tmp := cur.Left
        cur.Left = nil
        stack = append(stack, cur)
        cur = tmp
    }
    stack = append(stack, cur)
    return BSTIterator{stack}
}

/* ["BSTIterator","hasNext","next","hasNext","next","hasNext"]
[[[1,null,2]],[],[],[],[],[]] */

func (this *BSTIterator) Next() int {
    l   := len(this.Stack)
    if l == 0 {
        return 0
    }
    
    res := this.Stack[l-1]
    fmt.Println(res.Val)
    this.Stack = this.Stack[:l-1]

    var save *TreeNode = nil
    
    if res.Right != nil {
        save = res.Right
    } 
    
    if save != nil {
        cur := save.Left
        save.Left = nil
        this.Stack = append(this.Stack, save)
        for cur != nil {
            tmp := cur.Left
            cur.Left = nil
            this.Stack = append(this.Stack, cur)
            cur = tmp
        } 
        
    } 
    return res.Val
}


func (this *BSTIterator) HasNext() bool {
    if len(this.Stack) > 0 {
        return true
    } else {
        return false
    }
}


/**
 * Your BSTIterator object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */
