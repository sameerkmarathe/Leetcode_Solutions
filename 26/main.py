######################################################################
###############	26. Remove Duplicates From Array	##############
######################################################################


'''
Replace the duplicate with last unique elements and repeat till EOA
Time Complexity: O(n) n is the length of array and each element is visited once
Space Complexity:O(1) as we only keep constant space pointers in
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        prev = 0
        currIndex = 0
        
        for i,val in enumerate(nums):
            if i == 0:
                prev = val
                currIndex = 1
            else:
                if val == prev:
                    continue
                else:
                    nums[currIndex] = val
                    prev = val
                    currIndex += 1
                
                    
        return currIndex
