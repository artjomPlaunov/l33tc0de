func subarraySum(nums []int, k int) int {
    res, sum := 0,0
    hash := make(map[int]int)
    
    // set hash[0] to 1 for the case where sum == k => sum-k = 0
    hash[0] = 1
    
    for _, v := range nums {
        sum += v
        if count, ok := hash[sum-k]; ok {
            res += count
        }
        hash[sum] += 1
    }
    return res
}
