#####################################################
###########	39. Combination Sum	#############
#####################################################


'''
Classic DP problem where you fill up the elements with all numbers till target and recurse on the target-sum of current list
Time Complexity: O(n^2), we iterate and make list for all combinations of numbers in worst case
Space Complexity:O(n^2) as well because of number of combination
'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        dp: list = [[[]]] + [[] for i in range(target)] 
        for n in nums: 
            for s in range(n, target + 1):  
                li = [l + [n] for l in dp[s - n]] 
                dp[s] += li
        return dp[target]
