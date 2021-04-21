###########################################################
########	41. First Missing Positive	###########
###########################################################



'''
We rearrange the numbers to put them in their index. Then loop over to check if any of them does not exist. The trick is that the missing number will always be in range 1,..n+1.
Time Complexity: O(n) because we iterate over all elements
Space Complexity: O(n) because we keep extra array
'''


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i]-1 in range(n) and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                
        return ([i == nums[i]-1 for i in range(n)] + [0]).index(False) + 1 
