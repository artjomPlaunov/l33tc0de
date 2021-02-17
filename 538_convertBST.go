/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func helper(root *TreeNode, accum int) int{
    if root == nil {
        return accum
    } 
    if root.Right != nil {
        accum = helper(root.Right, accum)
    }
    root.Val += accum
    if root.Left != nil {
        accum = helper(root.Left, root.Val)
        return accum
    } else {
        return root.Val
    }
     
}

func convertBST(root *TreeNode) *TreeNode {
    _ = helper(root, 0)
    return root
}
