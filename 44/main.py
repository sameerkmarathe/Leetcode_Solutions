######################################################
########	44. Wildcard Matching	##############
######################################################


'''
Use DP. Move forward if next character matches and previous sequence matched. return last result
Default condition is true and empty string matches itself
Time Complexity: O(m*n) where m and n are length of patterns
Space Complexity:O(n) where n is the longest string
'''

class Solution:
def isMatch(self, s, p):
    length = len(s)
    if len(p) - p.count('*') > length:
        return False
    dp = [True] + [False]*length
    for i in p:
        if i != '*':
            for n in reversed(range(length)):
                dp[n+1] = dp[n] and (i == s[n] or i == '?')
        else:
            for n in range(1, length+1):
                dp[n] = dp[n-1] or dp[n]
        dp[0] = dp[0] and i == '*'
    return dp[-1]

'''
There is neat bit maunipulation trick to solve this in O(m+n). Credits to @daviscyl
'''

from collections import defaultdict
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        nexts = 1
        end_bit = 1<<len(s)
        d = defaultdict(int)
        for i,c in enumerate(s):
            d[c] |= 1<<i
        for c in p:
            if c == '*':
                nexts =  (end_bit<<1) - (nexts & -nexts)
            elif c == '?':
                nexts <<= 1
            else:
                nexts = (nexts & d[c]) << 1
            if nexts == 0:
                return False
        return nexts & end_bit != 0
