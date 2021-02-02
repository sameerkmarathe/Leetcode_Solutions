/**
*		4. Longest Palimdromic Substring	
**/


/*
This is in a way extension to two pointer approach discussed in problem 4. The approach is simple.
Just start at an index in string and extend outward till the substring ceases to be palindrome.
Time Complexity: O(n^2) because we can in worst case sweep entire string per index
Space Complexity: O(1) because we use constant amount of space to maintain the longest palindrome substring.
*/
class Solution {
    public String longestPalindrome(String s) {
  int n = s.length();
  String res = null;
    
  boolean[][] dp = new boolean[n][n];
    
  for (int i = n - 1; i >= 0; i--) {
    for (int j = i; j < n; j++) {
      dp[i][j] = s.charAt(i) == s.charAt(j) && (j - i < 3 || dp[i + 1][j - 1]);
            
      if (dp[i][j] && (res == null || j - i + 1 > res.length())) {
        res = s.substring(i, j + 1);
      }
    }
  }
    
  return res;
	}
}

/*
Another cool linear approach to this is manchester algorithm. The code for that approach can be referred here:
https://leetcode.com/problems/longest-palindromic-substring/discuss/3337/Manacher-algorithm-in-Python-O(n)
*/


