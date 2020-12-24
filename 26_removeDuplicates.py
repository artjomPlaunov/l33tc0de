class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        insert = 0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                continue
            else:
                nums[insert] = nums[i]
                insert += 1
        nums[insert] = nums[-1]
        return insert+1
