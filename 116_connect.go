/**
 * Definition for a Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Next *Node
 * }
 */

func connect(root *Node) *Node {
    
    if root == nil {
        return root
    }
    
    curLevel := root
    nextLevel := root.Left
    
    for nextLevel != nil {
        for curLevel != nil {
            curLevel.Left.Next = curLevel.Right
            if curLevel.Next != nil {
                curLevel.Right.Next = curLevel.Next.Left
            }
            curLevel = curLevel.Next
        }
        curLevel = nextLevel
        nextLevel = curLevel.Left
    }
    return root
}
