/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func max(x,y int) int {
    if x > y {
        return x
    } else {
        return y
    }
}

func getMaxDepths(root *TreeNode, hash map[*TreeNode]int) {
    if root == nil {
        return
    }
    getMaxDepths(root.Left, hash)
    getMaxDepths(root.Right, hash)
    if root.Left != nil && root.Right != nil {
        hash[root] = max(hash[root.Left], hash[root.Right]) + 1
    } else if root.Left != nil {
        hash[root] = hash[root.Left] + 1
    } else if root.Right != nil {
        hash[root] = hash[root.Right] + 1
    } else {
        hash[root] = 0
    }
}

func subtreeWithAllDeepest(root *TreeNode) *TreeNode {
    if root == nil {
        return root
    }
    
    hash := make(map[*TreeNode]int)
    getMaxDepths(root, hash)
    
    cur := root
    for cur.Left != nil || cur.Right != nil {
        if cur.Left == nil {
            cur = cur.Right
        } else if cur.Right == nil {
            cur = cur.Left
        } else {
            if hash[cur.Left] > hash[cur.Right] {
                cur = cur.Left
            } else if hash[cur.Right] > hash[cur.Left] {
                cur = cur.Right
            } else {
                return cur
            }
        }
    }
    return cur
}


