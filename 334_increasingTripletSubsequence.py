class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        
        i = self.findFirstDownEdge(nums)
        if i < 0:
            return False
        maxDownEdge = (nums[i],nums[i+1])
        
        while i >= 1:
            (lo,hi) = maxDownEdge
            if nums[i-1] < lo:
                return True
            elif (nums[i-1] > nums[i]):
                if nums[i-1] > lo and nums[i-1] < hi:
                    maxDownEdge = (nums[i-1], hi)
            elif nums[i-1] < nums[i]:
                if nums[i] > hi:
                    maxDownEdge = (nums[i-1],nums[i])
            i -= 1
            
        return False
    
    def findFirstDownEdge(self, nums):
        l,r = len(nums)-2,len(nums)-1
        while l >= 0 and (nums[l] >= nums[r]):
            l,r = l-1, r-1
        return l
