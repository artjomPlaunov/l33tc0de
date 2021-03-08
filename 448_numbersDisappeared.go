func findDisappearedNumbers(nums []int) []int {
    for i,_ := range nums {
        for nums[i] != i+1 { 
            v := nums[i]
            if v == nums[v-1] {
                break
            } else {
                nums[i], nums[v-1] = nums[v-1],nums[i]
                
            }
            
        }
    }
    res := make([]int, 0)
    for i,v := range nums {
        if i != v-1 {
            res = append(res, i+1)
        }
    }
    return res
}

