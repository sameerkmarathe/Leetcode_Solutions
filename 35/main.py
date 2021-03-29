##########################################################
##############	35. Search Insert Position	##########
##########################################################


'''
Common binary search with a twist. If element is not present it can always be added to the leftmost position in the window. The final window before while loop shows index where the next element is just
greater than target element.
Time Complexity:O(logn) where n is the length of the array
Space Complexity:O(1) as we keep constant space for all indices
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
