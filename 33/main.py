##################################################################
###########	33. Search in Rotated Sorted Array	##########
##################################################################



'''
The logic is the same as always. The only difference is that we will have to look at the pivot element. Since pivot can be anything we add two additional conditions of clipping which are very evident after a glance at code
Time Complexity: O(logn) where n is the length of array
Space Complexity: O(1) to store pointers
'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi  = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo+hi) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= target < nums[mid] or target < nums[mid] < nums[0] or nums[mid] < nums[0] <= target:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1
        
