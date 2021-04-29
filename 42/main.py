################################################################
########	42. Trapping Rain Water 	################
################################################################



'''
The approach is same as we will do in real life. Go from left and start filling water till we cannot
Time Complexity: O(n) as we look at each height once
Space Complexity:O(1) As we use constant space always
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        h1 = 0
        h2 = 0
        for i in range(len(height)):
            h1 = max(h1,height[i])
            h2 = max(h2,height[-i-1])
            ans = ans + h1 + h2 -height[i]
        return  ans - len(height)*h1
                
