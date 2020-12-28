func trap(height []int) int {
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
}
