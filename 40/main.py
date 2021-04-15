#######################################################################
#########	40. Combination Sum II	###############################
#######################################################################


'''
This is the same problem as 39. The only difference is the use of set instead of list
Time Complexity and Space Complexity remains the same as before
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp = [set() for i in range(target+1)]
        dp[0].add(())
        for num in candidates:
            for t in range(target, num-1, -1):
                for prev in dp[t-num]:
                    dp[t].add(prev + (num,))
        return list(dp[-1])
