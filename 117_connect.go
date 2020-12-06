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
    
    /*  Ternary Operator to traverse to next level, set to left if non-nil, 
        otherwise set to right (nil or non-nil) */
    setNext := func(cur *Node) *Node {
        if cur.Left != nil {
            return cur.Left
        } else {
            return cur.Right
        }
        
    }
    
    /* Traverse current level and find the left-most child */
    getNextChild := func(cur *Node) *Node {
        for cur != nil {
            if cur.Left != nil {
                return cur.Left 
            } else if cur.Right != nil {
                return cur.Right
            } else {
                cur = cur.Next
            }
        }
        return nil
    }
    
    curLevel := root
    nextLevel := setNext(curLevel)
    
    for nextLevel != nil {
        for curLevel != nil {
            nextChild := getNextChild(curLevel.Next)
            if curLevel.Left != nil && curLevel.Right != nil {
                curLevel.Left.Next = curLevel.Right
                curLevel.Right.Next = nextChild
            } else if curLevel.Left != nil {
                curLevel.Left.Next = nextChild
            } else if curLevel.Right != nil {
                curLevel.Right.Next = nextChild
            }
            curLevel = curLevel.Next
        }
        curLevel = nextLevel
        nextLevel = getNextChild(nextLevel)
    }
    return root
}
