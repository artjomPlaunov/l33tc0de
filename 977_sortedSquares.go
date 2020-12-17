import "math"

func sortedSquares(nums []int) []int {
    i := 0
    res := make([]int,0)
    lo,hi := -1,-1
    
    for i < len(nums) {
        if nums[i] == 0 {
            res = append(res, 0)
            lo = i-1
            i += 1
            for i < len(nums) {
                if nums[i] == 0 {
                    res = append(res,0)
                    i += 1
                } else {
                    break
                }
            
            }            
            hi = i
            break
        } else if nums[i] >= 0 {
            lo = i-1
            hi = i
            break
        } else if i == len(nums)-1 {
            lo = len(nums)-1
            hi = len(nums)
        }
        i += 1
    }
    
    for lo >= 0 && hi < len(nums) {
        num1 := int(math.Pow(float64(nums[lo]), 2.0))
        num2 := int(math.Pow(float64(nums[hi]), 2.0))
        
        if num1 < num2 {
            res = append(res, num1)
            lo -= 1
        } else {
            res = append(res, num2)
            hi += 1
        }
    }
    for lo >= 0 {
        num := int(math.Pow(float64(nums[lo]),2.0))
        res = append(res, num)
        lo -= 1
    }
    for hi < len(nums) {
        num := int(math.Pow(float64(nums[hi]),2.0))
        res = append(res, num)
        hi += 1
    }
    return res
}
