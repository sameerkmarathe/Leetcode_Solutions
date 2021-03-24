########################################################################################
############	34. Find First and Last Position of Element in Sorted Array	########
########################################################################################



'''
Perform binary search on first half and second half of array. Return the maximum index from calls
Time Complexity:O(logn) because we do binary search
Space Complexity:O(1) because we store the indices
'''


class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1,-1]
        def search(lo, hi):
            if nums[lo] == target == nums[hi]:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mid = (lo + hi) // 2
                l, r = search(lo, mid), search(mid+1, hi)
                return max(l, r) if -1 in l+r else [l[0], r[1]]
            return [-1, -1]
        return search(0, len(nums)-1)
