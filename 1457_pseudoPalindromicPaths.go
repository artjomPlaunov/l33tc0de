/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func pseudoPalindromicPaths (root *TreeNode) int {
    if root == nil {
        return 0
    }
    return aux(root, make(map[int]int), 0)
}

func aux(root *TreeNode, hash map[int]int, singles int) int {
    res := 0
    c := root.Val
    hash[c] += 1
    
    if hash[c] % 2 == 1 {
        singles += 1
    } else {
        singles -= 1 
    }
    
    if root.Left == nil && root.Right == nil {
        if singles <= 1 {
            res += 1
        }
    } else {
        if root.Left != nil {
            res += aux(root.Left, hash, singles)
        }
        if root.Right != nil {
            res += aux(root.Right, hash, singles)
        }
    }
    hash[c] -= 1
    return res
}
