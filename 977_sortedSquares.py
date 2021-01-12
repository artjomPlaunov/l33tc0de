class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        j = 0
        while j < len(nums) and nums[j] < 0:
            j += 1
        
        i = j-1
        while j < len(nums) and nums[j] == 0:
            res.append(0)
            j += 1
        
        while i >= 0 and j < len(nums):
            if nums[i]**2 < nums[j]**2:
                res.append(nums[i]**2)
                i -= 1
            else:
                res.append(nums[j]**2)
                j += 1
        
        while i >= 0:
            res.append(nums[i]**2)
            i -= 1
        while j < len(nums):
            res.append(nums[j]**2)
            j += 1
        return res
