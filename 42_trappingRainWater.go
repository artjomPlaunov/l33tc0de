func max(x,y int) int {
    if x > y {
        return x
    } else {
        return y
    }
}

func min(x,y int) int {
    if x < y {
        return x
    } else {
        return y
    }
}


func trap(height []int) int {
    
    if len(height) == 0 {
        return 0
    }
    
    maxSeenRight := make([]int,len(height))
    maxRight := height[len(height)-1]
    for i := len(height)-2; i >= 1; i-- {
        if height[i+1] > maxRight {
            maxRight = height[i+1]
        }
        maxSeenRight[i] = maxRight
    } 
    maxSeenLeft := height[0]
    res := 0
    for i := 1; i < len(height)-1; i++ {
        res += max(min(maxSeenLeft,maxSeenRight[i])-height[i],0)
        if height[i] > maxSeenLeft {
            maxSeenLeft = height[i]
        }
    }
    return res

    /*  O(MN) solution, where M is the max height in the array and N is length of 
        array.
    max := 0
    for _,v := range height {
        if v > max {
            max = v
        }
    }
    res := 0
    for i := 1; i <= max; i++ {
        start := 0
        for height[start] < i {
            start += 1
        }
        end := start+1
        for end < len(height) {
            for end < len(height) && height[end] < i {
                end += 1
            }
            if end < len(height) {
                res += (end-start-1)
            }
            start = end
            end = start+1
        }
    }
    return res
    */
}
