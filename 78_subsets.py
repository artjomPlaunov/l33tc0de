class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Iterative solution
        result = [[]]
        for num in nums:
            for i in range(len(result)):
                newSet = copy.deepcopy(result[i])
                newSet.append(num)
                result.append(newSet)
        return result
        
        # Recursive solution
        # return self.helper(nums)

    def helper(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        res = self.helper(nums[1:])
        num = nums[0]
        for i in range(len(res)):
            newSet = copy.deepcopy(res[i])
            newSet.append(num)
            res.append(newSet)
        return res
