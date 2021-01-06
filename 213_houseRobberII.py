from collections import defaultdict

class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict(int)
        self.dp(0, nums, memo, True)
        return max(memo[(True,0)], memo[(False,0)])
    
    def dp(self, index, nums, memo, flag):
        if (flag,index) in memo:
            return
        elif index >= len(nums):
            return
        elif index == len(nums)-1 and index > 0:
            if flag:
                memo[(flag,index)] = 0
            else:
                memo[(flag,index)] = nums[index]
            return
        elif index == 0:
            self.dp(index+2, nums, memo, True)
            self.dp(index+1, nums, memo, False)
            val = nums[0]
            memo[(True,0)] = val + memo[(True,2)]
            memo[(False,0)] = memo[(False,1)]
        else:
            self.dp(index+1, nums, memo, flag)
            self.dp(index+2, nums, memo, flag)
            val = nums[index]
            memo[(flag,index)] = max(val+memo[(flag,index+2)], memo[(flag,index+1)])
               
        
