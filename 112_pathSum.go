/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Accum struct {
    Node    *TreeNode
    Sum     int
}

func hasPathSum(root *TreeNode, targetSum int) bool {
    
    if root == nil {
        return false
    }
    
    stk := make([]Accum, 0)
    stk = append(stk, Accum{root, 0})
    
    for len(stk) > 0 {
        top := stk[len(stk)-1]
        stk = stk[:len(stk)-1]

        if top.Node.Left == nil && top.Node.Right == nil {
            if top.Node.Val + top.Sum == targetSum {
                return true
            }
        } else {
            if top.Node.Left != nil {
                stk = append(stk, Accum{top.Node.Left, top.Sum + top.Node.Val})
            }
            if top.Node.Right != nil {
                stk = append(stk, Accum{top.Node.Right, top.Sum + top.Node.Val})
            }
        }  
    }
    return false
}
