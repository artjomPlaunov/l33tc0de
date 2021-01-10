class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        seen = 0
        if arr[0] > 1:
            seen += arr[0]-1
        
        if seen >= k:
            return k
        
        for i in range(0, len(arr)-1):
            seen += arr[i+1]-arr[i]-1
            if seen >= k:
                j = seen-k
                return arr[i+1]-j-1
        
        return arr[-1] + (k-seen)
