func missingNumber(nums []int) int {
    found := false 
    for i,v := range nums {
        if v == len(nums) {
            found = true
            nums[i] = -1
        }
    }
    if !found {
        return len(nums)
    }
    
    for i,v := range nums {
        if v != -1 {
            for nums[i] != -1 && nums[i] != i {
                nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
            }
        }   
    }
    for i,v := range nums {
        if v == -1 {
            return i
        }
    }
    return -1
}
