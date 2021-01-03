##################################################################################
##############		4. Longest Palimdromic Substring	##################
##################################################################################


'''
This is in a way extension to two pointer approach discussed in problem 4. The approach is simple. Just start at an index in string and extend outward till the substring ceases to be palindrome.
Time Complexity: O(n^2) because we can in worst case sweep entire string per index
Space Complexity: O(1) because we use constant amount of space to maintain the longest palindrome substring.
'''

n = len(s)
def helper(s,l,r,n):
  while l>=0 and r < n and s[l]==s[r]:
    l-=1 ; r+=1
    return s[l+1:r]
res = ""
for i in range(n):
  res = max(helper(s,i,i,n), helper(s,i,i+1,n), res, key=len)

return res

'''
Another cool linear approach to this is manchester algorithm. The code for that approach can be referred here:
https://leetcode.com/problems/longest-palindromic-substring/discuss/3337/Manacher-algorithm-in-Python-O(n)
'''


