class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[], [nums[0]]]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                for j in range(len(res)-count, len(res)):
                    newSet = copy.deepcopy(res[j])
                    newSet.append(nums[i])
                    res.append(newSet)
            else:
                count = len(res)
                for j in range(len(res)):
                    newSet = copy.deepcopy(res[j])
                    newSet.append(nums[i])
                    res.append(newSet)
        return res
