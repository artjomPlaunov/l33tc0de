/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func averageOfLevels(root *TreeNode) []float64 {
    res := make([]float64, 0)
    Q := []*TreeNode{root}
    
    for len(Q) > 0 {
        curLen := len(Q)
        sum := 0.0
        newLevel := make([]*TreeNode, 0)
        for i := 0; i < curLen; i++ {
            sum += float64(Q[i].Val)
            if Q[i].Left != nil {
                newLevel = append(newLevel, Q[i].Left)
            }
            if Q[i].Right != nil {
                newLevel = append(newLevel, Q[i].Right)
            }
        }
        Q = newLevel
        res = append(res, sum/float64(curLen))
    }
    return res
}
