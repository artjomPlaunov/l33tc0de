func removeDuplicates(nums []int) int {
    next, dup := 0,false
    
    for forward := 0; forward < len(nums); forward++ {
        
        if forward == len(nums)-1 {
            if dup {
                return next
            } else {
                nums[next] = nums[forward]
                return next+1

            }
        }
        if nums[forward] == nums[forward+1] {
            fmt.Println(forward, next,dup)
            if dup {
                continue
            } else {
                nums[next] = nums[forward]
                nums[next+1] = nums[forward]
                if forward+2 < len (nums) {
                    if nums[forward] == nums[forward+2] {
                        dup = true
                    } else {
                        dup = false
                    }
                }
                next += 2
                forward += 1
            }
        } else {
            if !dup {
                nums[next] = nums[forward]
                next += 1
            }
            dup = false
        }
    }
    return next
}
