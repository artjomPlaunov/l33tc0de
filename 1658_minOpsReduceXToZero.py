# Inverse of Maximum contiguous subarray sum equal to k
# S = sum of array
# x = desired sum (from prefix+suffix)
# S-x = maximum contiguous subarray sum

class Solution:
    def maxContSubarrayK(self, nums, k):
        if k == 0:
            return 0
        
        res, windowStart, windowSum =-1,0,0
        
        for windowEnd in range(len(nums)):
            if nums[windowEnd] > k:
                windowStart = windowEnd+1
                continue
            windowSum += nums[windowEnd]
            while windowSum > k:
                windowSum -= nums[windowStart]
                windowStart += 1
            
            if windowSum == k:
                res = max(res, windowEnd-windowStart+1)
        
        return res
    def minOperations(self, nums: List[int], x: int) -> int:

        S = 0
        for num in nums:
            S += num  
        k = S-x
        
        # Find length of maximum contiguous subarray equal to k => l
        # res = len(nums)-l
        l = self.maxContSubarrayK(nums, k)
        if l == -1:
            return -1
        return len(nums)-l
        
