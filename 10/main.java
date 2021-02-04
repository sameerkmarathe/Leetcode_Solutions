/**
*
*		10. Regular Expression Matching
*
**/


/*

This problem is understandable if you have idea about regex matching.
 Although a linear approach for this problem is difficult due to possibilities of regex arising.
 So we turn to DP and perform the matching by taking one character extra per iteration from the
 text
Time Complexity: O(product of string lengths) where strings represent the text and pattern
Space Complexity: O(minimum of length of two string) as we only need to memoize the results
 of the previous iteration and use it to build the current table. 
Note that this code was formulated from the explaination given in the solution.
Reference: https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation
*/


class Solution {
    public boolean isMatch(String s, String p) {

    if (s == null || p == null) {
        return false;
    }
    boolean[][] dp = new boolean[s.length()+1][p.length()+1];
    dp[0][0] = true;
    for (int i = 0; i < p.length(); i++) {
        if (p.charAt(i) == '*' && dp[0][i-1]) {
            dp[0][i+1] = true;
        }
    }
    for (int i = 0 ; i < s.length(); i++) {
        for (int j = 0; j < p.length(); j++) {
            if (p.charAt(j) == '.') {
                dp[i+1][j+1] = dp[i][j];
            }
            if (p.charAt(j) == s.charAt(i)) {
                dp[i+1][j+1] = dp[i][j];
            }
            if (p.charAt(j) == '*') {
                if (p.charAt(j-1) != s.charAt(i) && p.charAt(j-1) != '.') {
                    dp[i+1][j+1] = dp[i+1][j-1];
                } else {
                    dp[i+1][j+1] = (dp[i+1][j] || dp[i][j+1] || dp[i+1][j-1]);
                }
            }
        }
    }
    return dp[s.length()][p.length()];
}
}
