####################################################
########	27. Remove Element	############
####################################################


'''
Almost the same as last problem
Time Complexity:O(n) where n is the length of the array
Space Complexity:O(1) as we only work on origina; array
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        i,index=0,len(nums)-1
        
        while i<=index:
            if nums[i]==val:
                nums[i],nums[index]=nums[index],nums[i]
                index-=1
                
            else:
                i+=1
        return index+1
