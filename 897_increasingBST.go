/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func increasingBST(root *TreeNode) *TreeNode {
    stack := make([]*TreeNode,0)
    stack = append(stack, root)
    
    res := &TreeNode{}
    cur := res
    
    for len(stack) > 0 {
        l := len(stack)
        root = stack[l-1]
        stack = stack[:l-1]
        
        if root.Left == nil {
            cur.Right = root
            cur = cur.Right
            if root.Right != nil {
                stack = append(stack, root.Right)
                root.Right = nil
            }
        } else {
            stack = append(stack, root)
            stack = append(stack, root.Left)
            root.Left = nil
            
        }
    }
    return res.Right
}
